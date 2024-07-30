def generate_promotion_click(
    event_name,
    event_category,
    promotion_brand,
    promotion_id,
    promotion_name,
    promotion_list_name,
    promotion_position,
    promotion_type,
    screen_name,
    index,
):
    android_generator = """
// ANDROID
val promoParams = Bundle().apply {{
params.putString("event_category","{}");
params.putString("promotion_brand","{}"); // dynamic value
params.putString("promotion_id","{}"); // dynamic value // mandatory value
params.putString("promotion_name","{}"); // dynamic value // set empty string if null
params.putString("promotion_list_name","{}");  // dynamic value // set empty string if null
params.putString("promotion_position","{}"); // dynamic value // set 1 if null 
params.putString("promotion_type","{}"); // dynamic value //set empty string if null
params.putString("index", "1");
params.putString(Param.SCREEN_NAME,"{}"); // mandatory value
}}

firebaseAnalytics.logEvent("{}", promoParams)
""".format(
        event_category,
        promotion_brand,
        promotion_id,
        promotion_name,
        promotion_list_name,
        promotion_position,
        promotion_type,
        screen_name,
        event_name,
    )

    ios_generator = """
// IOS
Analytics.logEvent("promotion_click", parameters: [
"event_category":"{}",
"promotion_brand":"{}", // dynamic value // dynamic value
"promotion_id":"{}",  // dynamic value // mandatory value
"promotion_name":"{}", // dynamic value // set empty string if null
"promotion_list_name":"{}",  // dynamic value // set empty string if null
"promotion_position":"{}", // dynamic value // set 1 if null
"promotion_type":"{}", // dynamic value //set empty string if null
"index": "1",
AnalyticsParameterScreenName:"{}"
])
""".format(
        event_category,
        promotion_brand,
        promotion_id,
        promotion_name,
        promotion_list_name,
        promotion_position,
        promotion_type,
        screen_name,
    )
    print(android_generator)
    print(ios_generator)


def generate_view_item_list(
    event_name,
    event_category,
    screen_name,
    item_list_id,
    item_list_name,
    item_id,
    item_name,
    item_category,
    item_variant,
    item_brand,
    item_price,
):
    if event_name.upper() == "VIEW_ITEM_LIST":
        event_ios = "AnalyticsEventViewItemList"
    elif event_name.upper() == "SELECT_ITEM":
        event_ios = "AnalyticsEventSelectItem"
    elif event_name.upper() == "VIEW_ITEM":
        event_ios = "AnalyticsEventViewItem"

    android_generator = """
// ANDROID

// step 1 | Declare ecommerce items
// Adjust value based on available value
val itemShop1 = Bundle().apply {{
putString(FirebaseAnalytics.Param.ITEM_ID, "{}") // dynamic // mandatory value
putString(FirebaseAnalytics.Param.ITEM_NAME, "{}") // dynamic
putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "{}") // dynamic
putString(FirebaseAnalytics.Param.ITEM_VARIANT, "{}") //dynamic
putString(FirebaseAnalytics.Param.ITEM_BRAND, "{}") //dynamic
putDouble(FirebaseAnalytics.Param.PRICE, {})
}}

val itemShop2 = Bundle().apply {{
putString(FirebaseAnalytics.Param.ITEM_ID, "{}") // dynamic // mandatory value
putString(FirebaseAnalytics.Param.ITEM_NAME, "{}") // dynamic
putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "{}") // dynamic
putString(FirebaseAnalytics.Param.ITEM_VARIANT, "{}") //dynamic
putString(FirebaseAnalytics.Param.ITEM_BRAND, "{}") //dynamic
putDouble(FirebaseAnalytics.Param.PRICE, {})
}}

val itemShop2 = Bundle().apply {{
putString(FirebaseAnalytics.Param.ITEM_ID, "{}") // dynamic // mandatory value
putString(FirebaseAnalytics.Param.ITEM_NAME, "{}") // dynamic
putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "{}") // dynamic
putString(FirebaseAnalytics.Param.ITEM_VARIANT, "{}") //dynamic
putString(FirebaseAnalytics.Param.ITEM_BRAND, "{}") //dynamic
putDouble(FirebaseAnalytics.Param.PRICE, {})
}}


// step 2 | Add index to item, Please Adjust based on items shown in the page
val itemShop1WithIndex = Bundle(itemShop1).apply {{
putLong(FirebaseAnalytics.Param.INDEX, 1)
}}

val itemShop2WithIndex = Bundle(itemShop1).apply {{
putLong(FirebaseAnalytics.Param.INDEX, 2)
}}

val itemShop3WithIndex = Bundle(itemShop1).apply {{
putLong(FirebaseAnalytics.Param.INDEX, 3)
}}


// step 3 | Push the item using ecommerce events
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.{}) {{
param("event_category", "{}") // dynamic value // set empty string if null
param(FirebaseAnalytics.Param.SCREEN_NAME, "{}") // dynamic value // set empty string if null
param(FirebaseAnalytics.Param.ITEM_LIST_ID, "{}") // dynamic value // set empty string if null
param(FirebaseAnalytics.Param.ITEM_LIST_NAME, "{}") // dynamic
param(FirebaseAnalytics.Param.CURRENCY, "IDR") 
param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemShop1WithIndex, itemShop2WithIndex, itemShop3WithIndex),)
}}
""".format(
        item_id,
        item_name,
        item_category,
        item_variant,
        item_brand,
        item_price,
        item_id,
        item_name,
        item_category,
        item_variant,
        item_brand,
        item_price,
        item_id,
        item_name,
        item_category,
        item_variant,
        item_brand,
        item_price,
        event_name.upper(),
        event_category,
        screen_name,
        item_list_id,
        item_list_name,
    )

    ios_generator = """
// IOS
// step 1 | Declare ecommerce items
var itemShop1: [String: Any] = [
AnalyticsParameterItemID: "{}",
AnalyticsParameterItemName: "{}",
AnalyticsParameterItemCategory: "{}",
AnalyticsParameterItemVariant: "{}",
AnalyticsParameterItemBrand: "{}",
AnalyticsParameterPrice: {},
]

var itemShop2: [String: Any] = [
AnalyticsParameterItemID: "{}",
AnalyticsParameterItemName: "{}",
AnalyticsParameterItemCategory: "{}",
AnalyticsParameterItemVariant: "{}",
AnalyticsParameterItemBrand: "{}",
AnalyticsParameterPrice: {},
]

var itemShop3: [String: Any] = [
AnalyticsParameterItemID: "{}",
AnalyticsParameterItemName: "{}",
AnalyticsParameterItemCategory: "{}",
AnalyticsParameterItemVariant: "{}",
AnalyticsParameterItemBrand: "{}",
AnalyticsParameterPrice: {},
]


// step 2 | Add index to item, Please Adjust based on items shown in the page
itemShop1[AnalyticsParameterIndex] = 1
itemShop2[AnalyticsParameterIndex] = 2
itemShop3[AnalyticsParameterIndex] = 3

// step 3 | Push the item using ecommerce events
var itemList: [String: Any] = [
AnalyticsParameterScreenName:"{}"
AnalyticsParameterItemListID: "{}",
AnalyticsParameterItemListName: "{}",
AnalyticsParameterCurrency: "IDR"
]

itemList[AnalyticsParameterItems] = [itemShop1, itemShop2, itemShop3]
Analytics.logEvent({}, parameters: itemList)

""".format(
        item_id,
        item_name,
        item_category,
        item_variant,
        item_brand,
        item_price,
        item_id,
        item_name,
        item_category,
        item_variant,
        item_brand,
        item_price,
        item_id,
        item_name,
        item_category,
        item_variant,
        item_brand,
        item_price,
        screen_name,
        item_list_id,
        item_list_name,
        event_ios,
    )

    print(android_generator)
    print(ios_generator)


def generate_select_item_and_view_item(
    event_name,
    event_category,
    screen_name,
    item_list_id,
    item_list_name,
    item_id,
    item_name,
    item_category,
    item_variant,
    item_brand,
    item_price,
):
    if event_name.upper() == "VIEW_ITEM_LIST":
        event_ios = "AnalyticsEventViewItemList"
    elif event_name.upper() == "SELECT_ITEM":
        event_ios = "AnalyticsEventSelectItem"
    elif event_name.upper() == "VIEW_ITEM":
        event_ios = "AnalyticsEventViewItem"

    android_generator = """
// ANDROID

// step 1 | Declare ecommerce items
// Adjust value based on available value
val itemShop1 = Bundle().apply {{
putString(FirebaseAnalytics.Param.ITEM_ID, "{}") // dynamic // mandatory value
putString(FirebaseAnalytics.Param.ITEM_NAME, "{}") // dynamic
putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "{}") // dynamic
putString(FirebaseAnalytics.Param.ITEM_VARIANT, "{}") //dynamic
putString(FirebaseAnalytics.Param.ITEM_BRAND, "{}") //dynamic
putDouble(FirebaseAnalytics.Param.PRICE, {})
}}


// step 2 | Add index to item, Please Adjust based on items shown in the page
val itemShop1WithIndex = Bundle(itemShop1).apply {{
putLong(FirebaseAnalytics.Param.INDEX, 1)
}}


// step 3 | Push the item using ecommerce events
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.{}) {{
param("event_category", "{}") // dynamic value // set empty string if null
param(FirebaseAnalytics.Param.SCREEN_NAME, "{}") // dynamic value // set empty string if null
param(FirebaseAnalytics.Param.ITEM_LIST_ID, "{}") // dynamic value // set empty string if null
param(FirebaseAnalytics.Param.ITEM_LIST_NAME, "{}") // dynamic
param(FirebaseAnalytics.Param.CURRENCY, "IDR") 
param(FirebaseAnalytics.Param.VALUE, {}) // dynamic // price of product
param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemShop1WithIndex),)
}}
""".format(
        item_id,
        item_name,
        item_category,
        item_variant,
        item_brand,
        item_price,
        event_name.upper(),
        event_category,
        screen_name,
        item_list_id,
        item_list_name,
        item_price,
    )

    ios_generator = """
// IOS
// step 1 | Declare ecommerce items
var itemShop1: [String: Any] = [
AnalyticsParameterItemID: "{}",
AnalyticsParameterItemName: "{}",
AnalyticsParameterItemCategory: "{}",
AnalyticsParameterItemVariant: "{}",
AnalyticsParameterItemBrand: "{}",
AnalyticsParameterPrice: {},
]


// step 2 | Add index to item, Please Adjust based on items shown in the page
itemShop1[AnalyticsParameterIndex] = 1

// step 3 | Push the item using ecommerce events
var itemList: [String: Any] = [
AnalyticsParameterScreenName:"{}"
AnalyticsParameterItemListID: "{}",
AnalyticsParameterItemListName: "{}",
AnalyticsParameterCurrency: "IDR",
AnalyticsParameterValue: {} // dynamic // price of product
]

itemList[AnalyticsParameterItems] = [itemShop1]
Analytics.logEvent({}, parameters: itemList)

""".format(
        item_id,
        item_name,
        item_category,
        item_variant,
        item_brand,
        item_price,
        screen_name,
        item_list_id,
        item_list_name,
        item_price,
        event_ios,
    )

    print(android_generator)
    print(ios_generator)


def generate_button_click(
    event_name, event_category, button_name, button_purpose, screen_name
):
    android_generator = """
// ANDROID
val promoParams = Bundle().apply {{
params.putString("event_category","{}");
params.putString(Param.SCREEN_NAME,"{}"); // mandatory value
params.putString("button_name","{}"); // dynamic
params.putString("button_purpose","{}"); // dynamic
}}

firebaseAnalytics.logEvent("{}", promoParams)
""".format(
        event_category, screen_name, button_name, button_purpose, event_name
    )

    ios_generator = """
// IOS
Analytics.logEvent("{}", parameters: [
"event_category":"{}",
AnalyticsParameterScreenName:"{}",
"button_name": "{}", // dynamic
"button_purpose": "{}",
])
""".format(
        event_name, event_category, screen_name, button_name, button_purpose
    )
    print(android_generator)
    print(ios_generator)


def generate_section_click(event_name, event_category, list_name, screen_name):
    android_generator = """
// ANDROID
val promoParams = Bundle().apply {{
params.putString("event_category","{}");
params.putString(Param.SCREEN_NAME,"{}"); // mandatory value
params.putString("list_name","{}"); // dynamic
}}

firebaseAnalytics.logEvent("{}", promoParams)
""".format(
        event_category, screen_name, list_name, event_name
    )

    ios_generator = """
// IOS
Analytics.logEvent("{}", parameters: [
"event_category":"{}",
AnalyticsParameterScreenName:"{}",
"list_name": "{}"f
])
""".format(
        event_name, event_category, screen_name, list_name
    )
    print(android_generator)
    print(ios_generator)


def generate_screen_view(event_name, screen_name):
    if event_name == "screen_view":
        event_ios = "AnalyticsEventScreenView"
    android_generator = """
// ANDROID
val promoParams = Bundle().apply {{
params.putString(Param.SCREEN_NAME,"{}"); // mandatory value
params.putString(Param.SCREEN_CLASS, screenName); // using available value 
}}

firebaseAnalytics.logEvent(FirebaseAnalytics.Event.{}, promoParams)
""".format(
        screen_name, event_name.upper()
    )

    ios_generator = """
// IOS
Analytics.logEvent({}, parameters: [
AnalyticsParameterScreenName:"{}",
AnalyticsParameterScreenClass: screenClass,
])
""".format(
        event_ios,
        screen_name,
    )
    print(android_generator)
    print(ios_generator)
