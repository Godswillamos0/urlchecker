document.getElementById("sendBtn").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const currentTab = tabs[0];
    if (currentTab && currentTab.url) {
      fetch("https://your-api-endpoint.com/receive-url", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: currentTab.url })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById("status").innerText = "✅ Sent!";
      })
      .catch(err => {
        console.error(err);
        document.getElementById("status").innerText = "❌ Failed to send.";
      });
    }
  });
});
