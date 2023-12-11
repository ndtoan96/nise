from entities import ProductInfo, ValidateResult
import easyocr
import Levenshtein

BRAND_LC = "bosch"
READER = easyocr.Reader(["en", "vi"])
PRICE_THRESHOLD = 800000


def validateProduct(product: ProductInfo) -> ValidateResult:
    textIncludesBrand = (
        BRAND_LC in product.description.lower()
        or BRAND_LC in product.title.lower()
        or any(map(lambda x: BRAND_LC in x.lower(), product.properties.values()))
    )

    imageIncludesBrand = False
    for img in product.images:
        for _, text, confident in READER.readtext(img):
            textdiff = Levenshtein.ratio(text.lower(), BRAND_LC)
            print()
            print(f"text: {text}, confident: {confident}, diff: {textdiff}")
            if confident > 0.1 and textdiff > 0.5:
                imageIncludesBrand = True
                break
        if imageIncludesBrand:
            break

    mall = product.mall
    if "Tình trạng" in product.properties:
        oldProduct = product.properties["Tình trạng"].lower() == "đã sử dụng"
    else:
        oldProduct = False

    lowPrice = product.price[1] < PRICE_THRESHOLD

    isFake = (
        (textIncludesBrand or imageIncludesBrand)
        and not mall
        and not oldProduct
        and lowPrice
    )

    return ValidateResult(
        textIncludesBrand=textIncludesBrand,
        imageIncludesBrand=imageIncludesBrand,
        mall=mall,
        oldProduct=oldProduct,
        lowPrice=lowPrice,
        isFake=isFake,
    )
