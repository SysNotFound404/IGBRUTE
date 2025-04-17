class Useragent:

    def generate_useragent(self):

        # Daftar komponen yang bisa diacak

        app_versions = [

            "70.0.0.15.98","80.0.0.20.101","60.0.0.10.76","85.0.0.25.100","75.0.0.22.99","72.0.0.18.94","68.0.0.16.84","78.0.0.14.97","63.0.0.20.81","81.0.0.24.105","73.0.0.16.96","67.0.0.18.88","84.0.0.21.110","74.0.0.18.100","71.0.0.15.92","79.0.0.14.103","62.0.0.18.80","87.0.0.22.115","76.0.0.20.102","83.0.0.18.10","66.0.0.16.87","88.0.0.24.118","77.0.0.22.103","64.0.0.18.82","82.0.0.20.107","69.0.0.14.92","89.0.0.20.123","61.0.0.14.76","86.0.0.18.112","65.0.0.12.86"

        ]

        android_versions = [

            "29/10", "30/11", "28/9", "31/12", "32/13", "27/8"

        ]

        ios_versions = [

            "iOS 15.1", "iOS 16.0", "iOS 14.4", "iPadOS 16.2", "iOS 17.1"

        ]

        windows_versions = [

            "Windows 10", "Windows 11", "Windows 8.1"

        ]

        dpis = [

            "320dpi", "480dpi", "640dpi", "213dpi", "240dpi", "160dpi"

        ]

        resolutions = [

            "1080x2400", "720x1600", "1080x2340", "1440x3200",

            "1080x2280", "1080x1920", "720x1280", "1920x1080"

        ]

        languages = [

            "en_US", "id_ID", "zh_CN", "hi_IN", "ar_SA", "es_ES",

            "ru_RU", "pt_BR", "fr_FR", "ja_JP"

        ]



        models = {

    "vivo": [

        "vivo Y27", "vivo X100", "vivo V29", "vivo Y36", "vivo V23e", "vivo Y01", "vivo X90 Pro"

    ],

    "samsung": [

        "Galaxy S23", "Galaxy A14", "Galaxy Z Fold 5", "Galaxy Note 10", "Galaxy A54", "Galaxy M14", "Galaxy Z Flip 5"

    ],

    "meizu": [

        "Meizu 20", "Meizu M6s", "Meizu 18s", "Meizu C3", "Meizu Note 9", "Meizu 15", "Meizu 21 Pro"

    ],

    "oppo": [

        "OPPO Reno8", "OPPO A78", "OPPO Find X5 Pro", "OPPO F21 Pro", "OPPO A17", "OPPO A96", "OPPO Reno10"

    ],

    "xiaomi": [

        "Redmi Note 12", "Xiaomi 13", "Redmi Note 11 Pro", "Redmi 10C", "Xiaomi Mi 13 Lite", "Xiaomi Mi 12", "Xiaomi 13T Pro"

    ],

    "realme": [

        "Realme C55", "Realme GT Neo 5", "Realme 11 Pro+", "Realme Narzo 50", "Realme 10 Pro", "Realme GT 2", "Realme 9i"

    ],

    "infinix": [

        "Infinix Zero 5G", "Infinix Note 30", "Infinix Smart 7", "Infinix Zero 20", "Infinix Note 30 Pro", "Infinix Hot 30"

    ],

    "huawei": [

        "Huawei P60 Pro", "Huawei Mate 50", "Huawei Nova 11", "Huawei P50 Pocket", "Huawei Y90", "Huawei MatePad Pro", "Huawei Mate 50 Pro"

    ],

    "andromax": [

        "Andromax Prime", "Andromax G2", "Andromax R", "Andromax E3", "Andromax M3Y", "Andromax MiFi"

    ],

    "poco": [

        "Poco X5 Pro", "Poco M5", "Poco X3 GT", "Poco F5", "Poco F4 GT", "Poco M4 Pro", "Poco C55"

    ],

    "iphone": [

        "iPhone 15 Pro", "iPhone 14", "iPhone 15", "iPhone 12 Mini", "iPhone 13 Pro Max", "iPhone SE 2022"

    ],

    "ipad": [

        "iPad Pro M2", "iPad Air 2022", "iPad Mini 5", "iPad Pro 2024", "iPad 10th Gen", "iPad Air 6"

    ],

    "windows": [

        "Surface Pro 9", "Dell XPS 15", "HP Envy x360", "Lenovo Yoga 9i", "Acer Swift X", "Microsoft Surface Go 3"

    ],

    "nokia": [

        "Nokia G21", "Nokia X30", "Nokia C31", "Nokia G60", "Nokia 3.4", "Nokia XR20", "Nokia T20"

    ]

          

        }





        processors = {

            "vivo": ["sdm710", "mt6765", "dimensity800", "dimensity1200", "helioP35"],

            "samsung": ["exynos2100", "snapdragon888", "exynos9611"],

            "meizu": ["helioP70", "snapdragon845", "exynos9810"],

            "oppo": ["helioG95", "dimensity700", "snapdragon720G"],

            "xiaomi": ["snapdragon732G", "dimensity920", "helioG88"],

            "realme": ["snapdragon870", "helioG96", "dimensity1200"],

            "infinix": ["helioG80", "helioP22", "dimensity810"],

            "huawei": ["kirin9000", "kirin985", "snapdragon778G"],

            "andromax": ["snapdragon410", "snapdragon212"],

            "poco": ["snapdragon860", "snapdragon870", "dimensity810"],

            "iphone": ["A14 Bionic", "A15 Bionic", "A16 Bionic"],

            "ipad": ["M1", "A14 Bionic", "M2"],

            "windows": ["intel-i7", "amd-ryzen7", "intel-i5"],

            "nokia": ["snapdragon480", "helioP22"]

        }



        # Acak merek dan model perangkat

        brand = random.choice(list(models.keys()))

        model = random.choice(models[brand])

        processor = random.choice(processors[brand])



        # Pilih versi dan parameter lainnya secara acak

        app_version = random.choice(app_versions)

        dpi = random.choice(dpis)

        resolution = random.choice(resolutions)

        language = random.choice(languages)



        # Pilih versi Android, iOS, atau Windows berdasarkan merek

        if brand in ["iphone", "ipad"]:

            ios_version = random.choice(ios_versions)

            return f"Instagram {app_version} {ios_version} ({resolution}; {dpi}; {model}; {processor}; {language})"

        elif brand == "windows":

            windows_version = random.choice(windows_versions)

            return f"Instagram {app_version} {windows_version} ({resolution}; {dpi}; {model}; {processor}; {language})"

        else:

            android_version = random.choice(android_versions)

            return f"Instagram {app_version} Android ({android_version}; {dpi}; {resolution}; {brand}; {model}; {processor}; {language})"

    def useragent_api(self):

        return self.generate_useragent()

    

    def replace_instagram_with_barcelona(self,text):

        return text.replace("Instagram", "Barcelona")

    

    def useragent_threads(self):

        input_text = self.generate_useragent()

        output_text = self.replace_instagram_with_barcelona(input_text)

        return output_text
