from datetime import datetime
import os, subprocess, requests, asyncio, zoneinfo
import obspython as obs
from autoLive_Lib.clan import setClan, getClan, removeClan, isClanKey

async def cron_job():
    print('Current time: %s' % getCurrentTime())
    twitch_token_url = "https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials"
    token_rs = requests.post(twitch_token_url.format(getClan("twitch_clinet_id"), getClan("twitch_secret")))

    if token_rs.status_code < 299:
        token = token_rs.json()['access_token']
        
        headers = {
            'Client-ID': getClan("twitch_clinet_id"),
            'Authorization': 'Bearer {}'.format(token)
        }

        channelID = getClan("twitch_channel_id")
        if not isClanKey("twitch_usrId"):
            setClan("LiveStatus", False)
            twitch_get_channel_info_url = "https://api.twitch.tv/helix/users?login={}"
            channel_info = requests.get(url = twitch_get_channel_info_url.format(channelID), headers=headers)
            if channel_info.status_code <= 299:
                channel_info_response = channel_info.json()["data"][0]
                setClan("twitch_usrId", channel_info_response['id'])
                setClan("twitch_usrname", channel_info_response['display_name'])

                twitch_live_url = "https://api.twitch.tv/helix/streams?user_id={}".format(getClan("twitch_usrId"))
                await get_live_status_response(headers, twitch_live_url)
                print('Live channels: {} ({})'.format(channelID, getClan("twitch_usrname")))
        else:
            twitch_live_url = "https://api.twitch.tv/helix/streams?user_id={}".format(getClan("twitch_usrId"))
            await get_live_status_response(headers, twitch_live_url)
            print('Live channels: {} ({})'.format(channelID, getClan("twitch_usrname")))

    else:
        print('Error: Twitch Token API returned {}'.format(token_rs.json()))


async def get_live_status_response(headers, live_url):
    try: 
        status = requests.get(url = live_url, headers = headers)
        response = status.json()
        live_data = response['data']
        if live_data:
            if not getClan("LiveStatus"):
                await StartBrowser()
            if isClanKey("twitch_fail_number_loop"):
                removeClan("twitch_fail_number_loop")
        else:
            await StopBrowser(False)
    except Exception as e:
        print("Unable to get url {} due to {}: \n{}.".format(live_url, e.__class__, e))

async def StartBrowser():
    print("{} ({}) start streaming {}".format(getClan("twitch_channel_id"), getClan("twitch_usrname"), getCurrentTime()))
    
    setClan("LiveStatus", True)
    
    if not isClanKey("browserProcessYTStudio"):
        print("Start Browser To YTStudio...")
        browserProcessYTStudio = subprocess.Popen([getClan("browserPath"), f'--app=https://studio.youtube.com/channel/UC/livestreaming', '--chrome-frame', '--window-size=800,600', '--window-position=0,0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        setClan("browserProcessYTStudio", browserProcessYTStudio)
    
    await asyncio.sleep(20)
    if not isClanKey("browserProcess"):
        print("Start Browser To Twitch...")
        browserProcess = subprocess.Popen([getClan("browserPath"), f'--app=https://www.twitch.tv/{getClan("twitch_channel_id")}', '--chrome-frame', '--window-size=800,600', '--window-position=0,0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        setClan("browserProcess", browserProcess)

    await asyncio.sleep(10)
    if obs.obs_frontend_streaming_active() == False:
        print("Start Streaming...")
        obs.obs_frontend_streaming_start()

async def StopBrowser(ForcedStop):
    print("{} ({}) stop streaming {}".format(getClan("twitch_channel_id"), getClan("twitch_usrname"), getCurrentTime()))

    if getClan("LiveStatus") == True:
        if not ForcedStop:
            if not isClanKey("twitch_fail_number_loop"):
                setClan("twitch_fail_number_loop", getClan("twitch_fail_number"))
            fail_number = getClan("twitch_fail_number_loop")
            setClan("twitch_fail_number_loop", fail_number - 1)
        else:
            setClan("twitch_fail_number_loop", 0)

        if getClan("twitch_fail_number_loop") <= 0:
            setClan("LiveStatus", False)
            removeClan("twitch_fail_number_loop")
            
            if obs.obs_frontend_streaming_active() == True:
                print("Stop Browser...")
                obs.obs_frontend_streaming_stop()

            await asyncio.sleep(5)
            if isClanKey("browserProcessYTStudio"):
                print("Stop Streaming By YTStudio...")
                subprocess.Popen("taskkill /F /T /PID %i" % getClan("browserProcessYTStudio").pid , shell=True)
                removeClan("browserProcessYTStudio")

            await asyncio.sleep(5)
            if isClanKey("browserProcess"):
                print("Stop Streaming By Twitch...")
                subprocess.Popen("taskkill /F /T /PID %i" % getClan("browserProcess").pid , shell=True)
                removeClan("browserProcess")
            

def getCurrentTime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")