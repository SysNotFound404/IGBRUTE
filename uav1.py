import random

class Useragent:
    def generate_useragent(self):
        # Daftar komponen yang bisa diacak
        app_versions = [
            "275.1.0.16.72", "272.0.0.16.70", "271.1.0.15.69",
            "270.0.0.15.65", "269.0.0.23.64", "268.1.0.18.61"
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
                "vivo Y20", "vivo X70 Pro", "vivo V21", "vivo Y33s", "vivo V25e", "vivo Y91C", "vivo X60 Pro"
            ],
            "samsung": [
                "Galaxy S21", "Galaxy A12", "Galaxy Z Flip", "Galaxy Note 20", "Galaxy A72", "Galaxy M32", "Galaxy Z Fold 3"
            ],
            "meizu": [
                "Meizu 16th", "Meizu M5 Note", "Meizu 18 Pro", "Meizu C9", "Meizu X8", "Meizu 17", "Meizu 16X"
            ],
            "oppo": [
                "OPPO Reno6", "OPPO A54", "OPPO Find X3 Pro", "OPPO F11", "OPPO A15", "OPPO A92", "OPPO Reno5"
            ],
            "xiaomi": [
                "Redmi Note 11", "Xiaomi 12", "Redmi Note 10 Pro", "Redmi Note 9 Pro", "Xiaomi Mi 11 Lite", "Xiaomi Mi 10", "Xiaomi 11T Pro"
            ],
            "realme": [
                "Realme C21", "Realme GT Neo 2", "Realme 9 Pro+", "Realme X3", "Realme 8 Pro", "Realme X50", "Realme 7i"
            ],
            "infinix": [
                "Infinix Zero X", "Infinix Note 11", "Infinix Smart 5", "Infinix Zero Ultra", "Infinix Note 12", "Infinix Zero 8"
            ],
            "huawei": [
                "Huawei P40", "Huawei Mate 40 Pro", "Huawei Nova 9", "Huawei P30 Pro", "Huawei Y9a", "Huawei P20", "Huawei Mate 30 Pro"
            ],
            "andromax": [
                "Andromax A", "Andromax R2", "Andromax E2", "Andromax L", "Andromax Q", "Andromax ES"
            ],
            "poco": [
                "Poco X3 NFC", "Poco M3", "Poco X4 Pro", "Poco F3", "Poco F2 Pro", "Poco M2 Pro", "Poco C3"
            ],
            "iphone": [
                "iPhone 12 Pro", "iPhone 13", "iPhone 14 Pro", "iPhone XR", "iPhone 11", "iPhone SE 2020"
            ],
            "ipad": [
                "iPad Pro 12.9", "iPad Air 4", "iPad Mini 6", "iPad Pro 11", "iPad 9th Gen", "iPad Air 5"
            ],
            "windows": [
                "Surface Pro 7", "Dell XPS 13", "HP Spectre x360", "Lenovo ThinkPad", "Acer Aspire 5", "Microsoft Surface Laptop"
            ],
            "nokia": [
                "Nokia 5.3", "Nokia 8.1", "Nokia X20", "Nokia G10", "Nokia 6.2", "Nokia 7.2", "Nokia 2.4"
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
        
