from datetime import datetime
from autoLive_Lib.core import cron_job, getCurrentTime
from autoLive_Lib.cron import Tick, RunAt, InitLastTime
from autoLive_Lib.clan import setClan, getClan
import obspython as obs
import asyncio

# # ------------------------------------------------------------

def script_load(settings):
	setClan("browserPath", obs.obs_data_get_string(settings, "browser_path"))
	setClan("twitch_channel_id", obs.obs_data_get_string(settings, "twitch_channel_id"))
	setClan("twitch_clinet_id", obs.obs_data_get_string(settings, "twitch_clinet_id"))
	setClan("twitch_secret", obs.obs_data_get_string(settings, "twitch_secret"))
	setClan("twitch_fail_number", obs.obs_data_get_int(settings, "twitch_fail_number"))

	print("Script loading...")
	print('Script started at {}'.format(getCurrentTime()))
	InitLastTime()
	obs.timer_add(Tick, 1000 * 60)
	TasksArgs = [ 0, 5, 10, 15, 20 ,25 , 30 , 35, 40 , 45 ,50 , 55]
	for task in TasksArgs:
		RunAt(task, cron_job)
		
	asyncio.sleep(30)
	asyncio.run(cron_job())
# # ------------------------------------------------------------

def script_description():
 	return "Twitch Live Auto Streaming..."

def script_update(settings):
	setClan("browserPath", obs.obs_data_get_string(settings, "browser_path"))
	setClan("twitch_channel_id", obs.obs_data_get_string(settings, "twitch_channel_id"))
	setClan("twitch_clinet_id", obs.obs_data_get_string(settings, "twitch_clinet_id"))
	setClan("twitch_secret", obs.obs_data_get_string(settings, "twitch_secret"))
	setClan("twitch_fail_number", obs.obs_data_get_int(settings, "twitch_fail_number"))

def script_defaults(settings):
  	obs.obs_data_set_default_int(settings, "twitch_fail_number", 3)

def script_properties():
	props = obs.obs_properties_create()
	obs.obs_properties_add_text(props, "browser_path", "Browser Path", obs.OBS_TEXT_DEFAULT)
	obs.obs_properties_add_text(props, "twitch_channel_id", "Twitch ChannelId", obs.OBS_TEXT_DEFAULT)
	obs.obs_properties_add_text(props, "twitch_clinet_id", "Twitch ClientID", obs.OBS_TEXT_DEFAULT)
	obs.obs_properties_add_text(props, "twitch_secret", "Twitch Secret", obs.OBS_TEXT_DEFAULT)
	obs.obs_properties_add_int(props, "twitch_fail_number", "Twitch Live Status Fail Number", 1, 30, 1)
	return props
