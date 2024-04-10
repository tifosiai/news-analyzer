# Some configuration variables.

PAD_IDX = 0  # Padding index
UNK_IDX = 1  # Unknown word index

# Tags for the named entities.
UNIQUE_TAGS = ["İsim",  "İsim-Mürəkkəb_Ad", "İsim-Xüsusi" ,"Sifət", "Sifət-Azaltma", "Sifət-Çoxaltma", "Say", "Say-Qeyri_müəyyən_miqdar", "Əvəzlik",
                "Əvəzlik-Şəxs", "Əvəzlik-İnkar", "Feil", "Feil-İnkar", "Feil-Təsirli", "Feil-Sifət", "Feil-Bağlama","Zərf", "Qoş-Vasitə_birgə","Qoş-Zaman",
                "Qoş-Məsafə","Qoş-İstiqamət", "Qoş-Bənzətmə", "Qoş-Fərqləndirmə", "Qoş-İstinad", "Qoş-Səbəb_Məqsəd", "Qoş-Aidlik","Bağ-Birləşdirmə",
                "Bağ-Qarşılaşdırma", "Bağ-Bölüşdürmə", "Bağ-İştirak","Bağ-İnkarlıq", "Bağ-Aydınlaşdırma", "Bağ-Tabelilik", "Əd-Qüvvətləndirici",
                "Əd-Dəqiqləşdirici", "Əd-Məhdudlaşdırıcı", "Əd-Sual", "Əd-Əmr", "Əd-Arzu", "Əd-Təsdiq", "Əd-İnkar", "Modal", "Ni-Positiv",
                "Ni-Neqativ", "Ni-Çağırış", "Köməkçi_söz", "Digər", "Numerativ_söz", "B/İsim-Mürəkkəb_Ad", 'E/İsim-Mürəkkəb_Ad', "B/Feil", "E/Feil", "M/İsim-Mürəkkəb_Ad", "İsim/Qoş-Vasitə_birgə", "M/Feil",
                "B/Zərf", 'E/Zərf', 'B/Feil-Bağlama', 'E/Feil-Bağlama', 'B/Feil-Sifət', 'E/Feil-Sifət', 'B/Feil-Təsirli', 'E/Feil-Təsirli', 'İsim-Xüsusi/Qoş-Vasitə_birgə', 'B/Əvəzlik-İnkar',  'E/Əvəzlik-İnkar',
                'B/Əvəzlik',  'E/Əvəzlik', 'B/Sifət-Çoxaltma', 'E/Sifət-Çoxaltma', 'Feil/Qoş-Vasitə_birgə', 'B/Bağ-İştirak', 'E/Bağ-İştirak', 'B/Bağ-Tabelilik', 'E/Bağ-Tabelilik', 'B/Feil-İnkar', 'E/Feil-İnkar',
                'B/Sifət', 'E/Sifət', 'Zərf/Qoş-Məsafə', 'B/Say', 'M/Say', 'E/Say', 'B/Bağ-Bölüşdürmə', 'E/Bağ-Bölüşdürmə', 'İsim/Qoş-Məsafə', 'B/İsim', 'E/İsim', 'B/Modal', 'E/Modal', 'Əvəzlik/Qoş-Vasitə_birgə',
                'B/Digər', 'E/Digər', 'B/İsim-Xüsusi', 'E/İsim-Xüsusi', 'B/Say-Qeyri_müəyyən_miqdar', 'M/Say-Qeyri_müəyyən_miqdar', 'E/Say-Qeyri_müəyyən_miqdar', 'B/Sifət-Azaltma', 'E/Sifət-Azaltma', 'İsim/Qoş-Zaman',
                'M/Feil-İnkar', 'Say/Qoş-Zaman', 'B/Əd-Qüvvətləndirici', 'E/Əd-Qüvvətləndirici', 'M/Bağ-Tabelilik', 'M/Feil-Sifət', 'Əvəzlik-Şəxs/Qoş-Vasitə_birgə', 'Say/Qoş-Vasitə_birgə', 'İsim/Bağ-Qarşılaşdırma',
                'M/Modal', 'M/İsim-Xüsusi', 'Feil/Qoş-Aidlik', 'İsim/Bağ-Birləşdirmə', 'M/Feil-Təsirli', 'B/Qoş-Səbəb_Məqsəd', 'M/Qoş-Səbəb_Məqsəd', 'E/Qoş-Səbəb_Məqsəd', 'Feil-Təsirli/Qoş-Vasitə_birgə', "B/Bağ-İnkarlıq",
                "E/Bağ-İnkarlıq", 'M/Digər', 'B/Feil-İnkar/Feil-Sifət', 'E/Feil-İnkar/Feil-Sifət', 'M/Feil-Bağlama', 'M/Sifət', 'Sifət/Qoş-Məsafə', 'B/Bağ-Aydınlaşdırma', 'E/Bağ-Aydınlaşdırma', 'Əvəzlik/Qoş-Məsafə',
                'B/Əd-İnkar', 'E/Əd-İnkar', 'B/Bağ-Birləşdirmə', 'E/Bağ-Birləşdirmə', 'M/İsim', 'M/Zərf', 'Feil-İnkar/Bağ-Tabelilik', 'Feil/Bağ-Tabelilik', 'Feil/Qoş-Məsafə', 'B/Əd-Arzu', 'E/Əd-Arzu',
               'İsim-Mürəkkəb_Ad/Qoş-Vasitə_birgə', 'Bağ-İştirak/Zərf', 'Say/Digər', 'Digər/Qoş-Məsafə', 'İsim/Qoş-Səbəb_Məqsəd','Digər/Say','İsim/Digər', 'Feil/Digər', 'İsim-Xüsusi/Bağ-Birləşdirmə', 'Sifət/Qoş-Vasitə_birgə',
               'B/Ni-Positiv', 'E/Ni-Positiv', 'İsim/Qoş-İstinad', 'B/Köməkçi_söz', 'E/Köməkçi_söz', "Zərf/Qoş-Vasitə_birgə", 'İsim/Qoş-Bənzətmə', 'Əvəzlik-Şəxs/İsim', 'Digər/İsim', 'İsim/Zərf', 'Feil-Sifət/Qoş-Vasitə_birgə',
               'Numerativ_söz/Qoş-Məsafə', 'Feil/Əd-Sual', 'Say/Qoş-Məsafə', 'Köməkçi_söz/Əd-Sual', 'Say/Sifət', 'İsim/Say', 'Əvəzlik/Əd-Qüvvətləndirici', 'İsim-Xüsusi/Qoş-Məsafə', 'Əvəzlik-Şəxs/Qoş-Səbəb_Məqsəd',
               'Zərf/Əd-Qüvvətləndirici', 'Say-Qeyri_müəyyən_miqdar/Digər', 'İsim/Əd-Qüvvətləndirici', 'İsim/Say-Qeyri_müəyyən_miqdar', 'B/Ni-Çağırış', 'E/Ni-Çağırış', 'M/Əvəzlik', 'Sifət/Qoş-Bənzətmə', 'Feil/Əd-Qüvvətləndirici',
                'Əvəzlik/Əd-Sual', 'Feil-Sifət/Qoş-Məsafə', 'M/Bağ-Bölüşdürmə',  'B/Qoş-Zaman', 'E/Qoş-Zaman', 'Əvəzlik-Şəxs/Qoş-Bənzətmə', 'Digər/Say-Qeyri_müəyyən_miqdar', 'İsim/Əd-Sual', 'Say/Əd-Qüvvətləndirici',
               'Feil-Sifət/Əd-Sual', 'Sifət/Əd-Sual',  'B/Əd-Məhdudlaşdırıcı', 'E/Əd-Məhdudlaşdırıcı', 'Sifət/Bağ-Birləşdirmə']

tag2idx = {tag: idx for idx, tag in enumerate(UNIQUE_TAGS)}
idx2tag = {idx: tag for tag, idx in tag2idx.items()}
