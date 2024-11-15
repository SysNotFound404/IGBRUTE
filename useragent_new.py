import random

class Useragent:
    def __init__(self):
        self.versi_ig = f'{str(random.randint(90, 380))}.0.0.{str(random.randint(10, 60))}.{str(random.randint(90, 220))}'
        self.versi_andro = random.choice([
            "27/9", "27/10", "27/11", "27/12", "27/12", "27/13", "28/9", "28/10", "28/11", "28/12", "28/12",
            "28/13", "29/9", "29/10", "29/11", "29/12", "29/12", "29/13", "27/9", "30/10", "30/11", "30/12",
            "30/12", "30/13", "31/9", "31/10", "31/11", "31/12", "31/12", "31/13", "32/9", "32/10", "32/11",
            "32/12", "32/12", "32/13", "33/9", "33/10", "33/11", "33/12", "33/12", "33/13", "32/26", "34/26",
            "32/11", "34/12", "30/10", "34/12.0.1", "30/11.0.3"
        ])

    def ua_api(self):
        self.oppo = random.choice([
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 720x1456; OPPO; CPH1941; OP4B80L1; qcom; id_ID; 660142269)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 480dpi; 1080x2161; OPPO; CPH2109; OP4BA5L1; qcom; id_ID; 289692198)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 360dpi; 720x1445; OPPO; CPH2637; OP4F2F; mt6765; id_ID; 337202351)'
        ])
        self.memex = random.choice([
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 240dpi; 480x854; Vodafone; VF-696; smart_grand; mt6580; id_ID; 99640900)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 480dpi; 1080x1920; samsung; SM-A520F; a5y17lte; samsungexynos7880; id_ID; 99640911)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 240dpi; 480x782; Sony; C2105; C2105; qcom; id_ID; 99640900)'
        ])
        self.memek = random.choice([
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 720x1280; m-net; Power1; m-net; mt6580; id_ID; 99640905)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 240dpi; 480x854; MOBIWIRE/ALTICE; STARNAUTE3; STARNAUTE3; mt6580; id_ID; 99640900)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 480dpi; 1080x1776; WIKO; U FEEL PRIME; p7201; qcom; id_ID; 99640911)'
        ])
        self.meki = random.choice([
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 720x1280; LENOVO/Lenovo; Lenovo P1ma40; P1ma40; mt6735; id_ID; 99640905)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 1344x720; Xiaomi; Redmi 5; rosy; qcom; id_ID; 99640905)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 720x1184; DOOGEE; Y300; hct6735m_35gu_m0; mt6735; id_ID; 99640905)'
        ])
        self.kontol = random.choice([
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 640dpi; 1440x2560; motorola; XT1254; quark; qcom; id_ID; 99640911)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 480dpi; 1080x1920; Meizu; MX5; mx5; mt6795; id_ID; 99640911)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 480dpi; 1080x1920; Meizu; MX5; mx5; mt6795; id_ID; 99640911)'
        ])
        self.kintil = random.choice([
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 640dpi; 1440x2560; vivo; vivo Xplay5S; PD1516A; qcom; id_ID; 99640911)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 720x1280; LENOVO/Lenovo; Lenovo P1ma40; P1ma40; mt6735; id_ID; 99640905)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 720x1280; m-net; Power1; m-net; mt6580; id_ID; 99640905)'
        ])
        self.mekimamak = random.choice([
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 720x1280; Meizu; m2; m2; mt6735; id_ID; 99640905)',
            f'Instagram {self.versi_ig} (iPhone7,2; iOS 11_2_5; id_ID; id_ID; scale=2.00; gamut=normal; 750x1334)',
            f'Instagram {self.versi_ig} (iPhone7,2; iOS 11_1_2; id_ID; id_ID; scale=2.00; gamut=normal; 750x1334)'
        ])
        self.CROOT = random.choice([self.mekimamak, self.kintil, self.kontol, self.oppo, self.memek, self.memex, self.meki])
        return self.CROOT

Useragent()