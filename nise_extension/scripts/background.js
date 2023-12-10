chrome.action.onClicked.addListener(async () => {
    const [tab] = await chrome.tabs.query({ active: true, lastFocusedWindow: true });
    const response = await chrome.tabs.sendMessage(tab.id, { message: "collect" });
    let res = await fetch("http://127.0.0.1:8000/productInfo", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(response.productInfo)
    });
    console.log(await res.json());
});