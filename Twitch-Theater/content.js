const excludeUrl = [,
    /.*:\/\/dashboard\.twitch\.tv.*/,
    /.*:\/\/.*\.twitch\.tv\/settings\/.*/,
]
let loadingFailed = 120
window.addEventListener("load", () => {
    console.log("Plugin loaded ....")
    if (excludeUrl.some(url => window.location.href.match(url)))
        return

    console.log("Plugin Get Twitch Url")
    setTimeout(() => {
        const watchEl = document.querySelector('.channel-root--watch')
        if (watchEl) {
            toggleTheaterMode()
            return
        }
    
        const clickChannel = document.querySelector('.ScHalo-sc-18imt3g-0')
        if (!clickChannel) 
            return
        clickChannel.click()
        toggleTheaterMode()
    }, 2000)
});

setInterval(() => {
    if (excludeUrl.some(url => window.location.href.match(url)))
        return

    const loading = document.querySelector('.tw-loading-spinner')
    if (!loading) {
        loadingFailed = 120
        return
    }else {
        loadingFailed--
        console.log(`Player Loading Failed | Auto Refresh Second ${loadingFailed}`)
        if (loadingFailed >= 1)
            return
        
        location.reload()
        loadingFailed = 120
    }

    const errorBtn = document.querySelector('.ScCoreButtonDestructive-sc-ocjdkq-4')
    if (!loading) 
        return
    errorBtn.click()
}, 1000);


setInterval(() => {
    if (excludeUrl.some(url => window.location.href.match(url)))
        return

    const errorBtn = document.querySelector('.ScCoreButtonDestructive-sc-ocjdkq-4')
    if (!errorBtn) 
        return
    
    setTimeout(() => {
        console.log("Error Click Button")
        errorBtn.click()
    }, 500)
}, 2000);

function toggleTheaterMode() {
    setTimeout(() => {
        const chatBar = document.querySelector(`[data-a-target="right-column-chat-bar"]`)
        if (!chatBar)
            return
        const chatBtn = document.querySelector(`[data-a-target="right-column__toggle-collapse-btn"]`)
        if (!chatBtn)
            return
        chatBtn.click()
    }, 500);


    setTimeout(() => {
        const theaterMode = document.querySelector(`[data-a-target="player-theatre-mode-button"]`)
        if (!theaterMode)
            return

        theaterMode.click()
    }, 1000);
}