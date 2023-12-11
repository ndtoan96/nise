chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        if (request.message == "collect") {
            console.log("start collecting");
            const url = document.URL.split('?')[0];
            const title = document.querySelector("div._44qnta > span").textContent;
            const mall = document.querySelector("div._44qnta > svg.BSp\\+Yo") ? true : false;

            let price;
            const priceRaw = document.querySelector("div.pqTWkA").textContent;
            if (priceRaw.includes('-')) {
                price = priceRaw.split('-').map((s) => Number(s.replace('₫', '').replaceAll('.', '')));
            } else {
                const p = Number(priceRaw.replace('₫', '').replaceAll('.', ''));
                price = [p, p];
            }

            let basePrice;
            const basePriceRaw = document.querySelector("div.Y3DvsN")?.textContent;
            if (basePriceRaw != null) {
                if (basePriceRaw.includes('-')) {
                    basePrice = basePriceRaw.split('-').map((s) => Number(s.replace('₫', '').replaceAll('.', '')));
                } else {
                    const p = Number(basePriceRaw.replace('₫', '').replaceAll('.', ''));
                    basePrice = [p, p];
                }
            } else {
                basePrice = price;
            }

            let properties = {};
            for (property of document.querySelectorAll("div.dR8kXc")) {
                const label = property.querySelector("label").textContent;
                const value = property.querySelector("label+*").textContent;
                properties[label] = value;
            }

            const description = document.querySelector("div.f7AU53").textContent;

            const images = [...document.querySelectorAll("picture > img")].map((e) => e.src);

            const productInfo = {
                url, title, mall, basePrice, price, properties, description, images,
                category: "may khoan"
            };

            console.log(productInfo);
            sendResponse({productInfo});
        }
    }
);