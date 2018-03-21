# Bible source: http://ebible.org/kjv/kjvtxt.zip
# Titles are from: https://austinbiblechurch.com/sites/default/files/documents/oyttb/Bible_Chapter_Titles.pdf
import BiblePaths
import json
import zipfile
import GetUrl
import ErrorMsg
import time


class CreateChapterJson:
    def __init__(self, max_hours=168):
        self.bpath = BiblePaths.BiblePaths()
        self.gu = GetUrl.GetUrl()
        self.get_url = self.gu.fetch_url
        self.em = ErrorMsg.ErrorMsg()

        self.max_file_age_hours = max_hours
        self.data_OK = 200

        self.audio_xref = {
            # '1st Chronicles',
            # '1st Kings',
            # '1st Samuel',
            # '1st Timothy',
            # '2nd Chronicles',
            # '2nd Kings',
            # '2nd Samuel',
            # 'Amos',
            # 'Daniel',
            # 'Deuteronomy',
            # 'Ecclesiastes',
            # 'Esther',
            # 'Exodus',
            # 'Ezekiel',
            # 'Ezra',
            # 'Genesis',
            # 'Habakkuk',
            # 'Haggai',
            # 'Hosea',
            # 'Isaiah',
            # 'Jeremiah',
            # 'Job',
            # 'Joel',
            # 'Jonah',
            # 'Joshua',
            # 'Judges',
            # 'Lamentations',
            # 'Leviticus',
            # 'Malachi',
            # 'Micah',
            # 'Nahum',
            # 'Nehemiah',
            # 'Numbers',
            # 'Obadiah',
            # 'Proverbs',
            # 'Psalms',
            # 'Ruth',
            # 'Song of Solomon',
            # 'Zechariah',
            # 'Zephaniah',

            '1Corinthians': '1st Corinthians',
            '1Timothy': '2nd Timothy',
            '2Thessalonians': '2nd Thessalonians',
            'Colossians': 'Colossians',
            'James': 'James',
            'Mark': 'Mark',
            'Revelation': 'Revelation',
            '1John': '1st John',
            '2Corinthians': '2nd Corinthians',
            '2Timothy': '2nd Timothy',
            'Ephesians': 'Ephesians',
            'John': 'John',
            'Matthew': 'Matthew',
            'Romans': 'Romans',
            '1Peter': '1st Peter',
            '2John': '2nd John',
            '3John': '3rd John',
            'Galatians': 'Galatians',
            'Jude': 'Jude',
            'Philemon': 'Philemon',
            'Titus': 'Titus',
            '1Thessalonians': '1st Thessalonians',
            '2Peter': '2nd Peter',
            'Acts': 'Acts',
            'Hebrews': 'Hebrews',
            'Luke': 'Luke',
            'Philippians': 'Philippians'
        }

        self.book_xref = {
            '1st Chronicles': '1Chron.txt',
            '1st Corinthians': '1Cor.txt',
            '1st John': '1John.txt',
            '1st Kings': '1Kings.txt',
            '1st Peter': '1Peter.txt',
            '1st Samuel': '1Sam.txt',
            '1st Thessalonians': '1Thes.txt',
            '1st Timothy': '1Tim.txt',
            '2nd Chronicles': '2Chron.txt',
            '2nd Corinthians': '2Cor.txt',
            '2nd John': '2John.txt',
            '2nd Kings': '2Kings.txt',
            '2nd Peter': '2Peter.txt',
            '2nd Samuel': '2Sam.txt',
            '2nd Thessalonians': '2Thes.txt',
            '2nd Timothy': '2Tim.txt',
            '3rd John': '3John.txt',
            'Acts': 'Acts.txt',
            'Amos': 'Amos.txt',
            'Colossians': 'Col.txt',
            'Daniel': 'Daniel.txt',
            'Deuteronomy': 'Deut.txt',
            'Ecclesiastes': 'Eccl.txt',
            'Ephesians': 'Eph.txt',
            'Esther': 'Esther.txt',
            'Exodus': 'Exodus.txt',
            'Ezekiel': 'Ezekiel.txt',
            'Ezra': 'Ezra.txt',
            'Galatians': 'Gal.txt',
            'Genesis': 'Genesis.txt',
            'Habakkuk': 'Habakkuk.txt',
            'Haggai': 'Haggai.txt',
            'Hebrews': 'Hebrews.txt',
            'Hosea': 'Hosea.txt',
            'Isaiah': 'Isaiah.txt',
            'James': 'James.txt',
            'Jeremiah': 'Jeremiah.txt',
            'Job': 'Job.txt',
            'Joel': 'Joel.txt',
            'John': 'John.txt',
            'Jonah': 'Jonah.txt',
            'Joshua': 'Joshua.txt',
            'Jude': 'Jude.txt',
            'Judges': 'Judges.txt',
            'Lamentations': 'Lament.txt',
            'Leviticus': 'Lev.txt',
            'Luke': 'Luke.txt',
            'Malachi': 'Malachi.txt',
            'Mark': 'Mark.txt',
            'Matthew': 'Matthew.txt',
            'Micah': 'Micah.txt',
            'Nahum': 'Nahum.txt',
            'Nehemiah': 'Nehemiah.txt',
            'Numbers': 'Num.txt',
            'Obadiah': 'Obadiah.txt',
            'Philemon': 'Philemon.txt',
            'Philippians': 'Philip.txt',
            'Proverbs': 'Proverbs.txt',
            'Psalms': 'Psalms.txt',
            'Revelation': 'Rev.txt',
            'Romans': 'Romans.txt',
            'Ruth': 'Ruth.txt',
            'Song of Solomon': 'Song.txt',
            'Titus': 'Titus.txt',
            'Zechariah': 'Zech.txt',
            'Zephaniah': 'Zeph.txt',
        }

        with self.bpath.BookXref.open('w') as f:
            json.dump(self.book_xref ,f)

        self.Bible = {
            'Old Testament': {
                'Genesis': {
                    'mp3': '/home/norman/Blind/recordings/genesis.mp3',
                    '1': {
                        'chapter_title': 'Creation & Recreation'
                    },
                    '2': {
                        'chapter_title': 'Creation & Recreation Recap'
                    },
                    '3': {
                        'chapter_title': 'The Fall of Man'
                    },
                    '4': {
                        'chapter_title': 'Cain Murders Abel'
                    },
                    '5': {
                        'chapter_title': 'Genealogies'
                    },
                    '6': {
                        'chapter_title': 'The Flood'
                    },
                    '7': {
                        'chapter_title': 'The Flood'
                    },
                    '8': {
                        'chapter_title': 'The Flood'
                    },
                    '9': {
                        'chapter_title': 'The Rainbow & Capital Punishment'
                    },
                    '10': {
                        'chapter_title': ' Genealogies'
                    },
                    '11': {
                        'chapter_title': ' The Tower of Babel'
                    },
                    '12': {
                        'chapter_title': ' The Call of Abraham'
                    },
                    '13': {
                        'chapter_title': ' The Cowboy Conflict'
                    },
                    '14': {
                        'chapter_title': ' The Kidnapping of Lot'
                    },
                    '15': {
                        'chapter_title': ' Abraham Believed God'
                    },
                    '16': {
                        'chapter_title': ' Ishmael is Born'
                    },
                    '17': {
                        'chapter_title': ' Abram becomes Abraham'
                    },
                    '18': {
                        'chapter_title': ' Abraham prays for Sodom'
                    },
                    '19': {
                        'chapter_title': ' Sodom is destroyed'
                    },
                    '20': {
                        'chapter_title': ' Abraham lies about Serah at Gerar'
                    },
                    '21': {
                        'chapter_title': ' The Birth of Isaac'
                    },
                    '22': {
                        'chapter_title': 'The Offering of Isaac'
                    },
                    '23': {
                        'chapter_title': 'The Death of Sarah'
                    },
                    '24': {
                        'chapter_title': 'The Bride for Isaac'
                    },
                    '25': {
                        'chapter_title': 'The Death of Abraham'
                    },
                    '26': {
                        'chapter_title': 'Abrahamic Covenant Confirmed to Isaac'
                    },
                    '27': {
                        'chapter_title': 'Jacob-Esau Birthright Conflict'
                    },
                    '28': {
                        'chapter_title': 'Abrahamic Covenant Confirmed to Jacob'
                    },
                    '29': {
                        'chapter_title': 'Jacob Marries Leah & Rachel'
                    },
                    '30': {
                        'chapter_title': 'Jacob''s Cattle (method of breeding)'
                    },
                    '31': {
                        'chapter_title': 'Jacob Leaves Laban'
                    },
                    '32': {
                        'chapter_title': 'Jacob Becomes Israel'
                    },
                    '33': {
                        'chapter_title': 'Jacob''s Reunion with Esau'
                    },
                    '34': {
                        'chapter_title': 'The Distress of Dinah'
                    },
                    '35': {
                        'chapter_title': 'Rachel Dies, Isaac Dies'
                    },
                    '36': {
                        'chapter_title': 'The Generations of Esau'
                    },
                    '37': {
                        'chapter_title': 'Joseph''s Dream, Sold to Egypt'
                    },
                    '38': {
                        'chapter_title': 'The Shame of Judah'
                    },
                    '39': {
                        'chapter_title': 'Joseph, Potiphar, & Prison'
                    },
                    '40': {
                        'chapter_title': 'Joseph''s Butler-Baker Dream'
                    },
                    '41': {
                        'chapter_title': 'Joseph, Minister of Agriculture'
                    },
                    '42': {
                        'chapter_title': 'Joseph''s 10 Brothers to Egypt to buy corn'
                    },
                    '43': {
                        'chapter_title': 'Joseph''s 11 Brothers to Egypt to buy corn'
                    },
                    '44': {
                        'chapter_title': 'Benjamin''s Silver Cup'
                    },
                    '45': {
                        'chapter_title': 'Joseph Reveals All'
                    },
                    '46': {
                        'chapter_title': 'Jacob and family move to Egypt'
                    },
                    '47': {
                        'chapter_title': 'Joseph sells corn for land for Pharaoh'
                    },
                    '48': {
                        'chapter_title': 'Joseph''s Sons, Double Portion'
                    },
                    '49': {
                        'chapter_title': 'Jacob''s Evaluation of His Sons'
                    },
                    '50': {
                        'chapter_title': 'Bones of Joseph (Jacob & Joseph Die)'
                    }
                },
                'Exodus': {
                    'mp3': '/home/norman/Blind/recordings/exodus.mp3',
                    '1': {
                        'chapter_title': 'Slavery in Egypt'
                    },
                    '2': {
                        'chapter_title': 'The Birth of Moses'
                    },
                    '3': {
                        'chapter_title': 'The Burning Bush'
                    },
                    '4': {
                        'chapter_title': 'The Objections of Moses'
                    },
                    '5': {
                        'chapter_title': 'Increased Slavery'
                    },
                    '6': {
                        'chapter_title': 'Affirmation of Abrahamic Covenant'
                    },
                    '7': {
                        'chapter_title': 'The Ten Plagues -- part 1'
                    },
                    '8': {
                        'chapter_title': 'The Ten Plagues -- part 2'
                    },
                    '9': {
                        'chapter_title': 'The Ten Plagues -- part 3'
                    },
                    '10': {
                        'chapter_title': 'The Ten Plagues -- part 4'
                    },
                    '11': {
                        'chapter_title': 'The Ten Plagues -- part 5'
                    },
                    '12': {
                        'chapter_title': 'The Ten Plagues -- part 6'
                    },
                    '13': {
                        'chapter_title': 'Guidance by Pillar of Cloud & Fire'
                    },
                    '14': {
                        'chapter_title': 'Crossing of the Red Sea'
                    },
                    '15': {
                        'chapter_title': 'Wrong Kind of Water (Marah)'
                    },
                    '16': {
                        'chapter_title': 'Provision of Manna'
                    },
                    '17': {
                        'chapter_title': 'No Water Situation (Rephidim)'
                    },
                    '18': {
                        'chapter_title': 'Organization Man Jethro'
                    },
                    '19': {
                        'chapter_title': 'Arrival at Mt. Sinai'
                    },
                    '20': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 1'
                    },
                    '21': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 2'
                    },
                    '22': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 3'
                    },
                    '23': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 4'
                    },
                    '24': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 5'
                    },
                    '25': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 6'
                    },
                    '26': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 7'
                    },
                    '27': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 8'
                    },
                    '28': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 9'
                    },
                    '29': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 10'
                    },
                    '30': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 11'
                    },
                    '31': {
                        'chapter_title': 'Giving of Mosaic Law -- Part 12'
                    },
                    '32': {
                        'chapter_title': 'Golden Calf (Stone tablets broken)'
                    },
                    '33': {
                        'chapter_title': 'On to Canaan (Moses sees God)'
                    },
                    '34': {
                        'chapter_title': 'Second Tablets of Stone'
                    },
                    '35': {
                        'chapter_title': 'Tabernacle Parts Constructed -- Part 1'
                    },
                    '36': {
                        'chapter_title': 'Tabernacle Parts Constructed -- Part 2'
                    },
                    '37': {
                        'chapter_title': 'Tabernacle Parts Constructed -- Part 3'
                    },
                    '38': {
                        'chapter_title': 'Tabernacle Parts Constructed -- Part 4'
                    },
                    '39': {
                        'chapter_title': 'Tabernacle Parts Constructed -- Part 5'
                    },
                    '40': {
                        'chapter_title': 'The Tabernacle is Set Up'
                    }
                },
                'Leviticus': {
                    'mp3': '/home/norman/Blind/recordings/leviticus.mp3',
                    '1': {
                        'chapter_title': 'The Sweet Savor Offerings - Burnt Offering'
                    },
                    '2': {
                        'chapter_title': 'The Sweet Savor Offerings - Meal Offering'
                    },
                    '3': {
                        'chapter_title': 'The Sweet Savor Offerings - Peace Offering'
                    },
                    '4': {
                        'chapter_title': 'The Non-Sweet Savor Offerings - Sin Offering'
                    },
                    '5': {
                        'chapter_title': 'The Non-Sweet Savor Offerings - Trespass Offering'
                    },
                    '6': {
                        'chapter_title': 'How to Apply the Five Offerings -- Part 1'
                    },
                    '7': {
                        'chapter_title': 'How to Apply the Five Offerings -- Part 2'
                    },
                    '8': {
                        'chapter_title': 'Consecration of the Priests'
                    },
                    '9': {
                        'chapter_title': 'Beginning of the Priest''s Ministry'
                    },
                    '10': {
                        'chapter_title': 'Strange Fire -- Nadab & Abihu'
                    },
                    '11': {
                        'chapter_title': 'The Food of Israel'
                    },
                    '12': {
                        'chapter_title': 'The Law of Motherhood'
                    },
                    '13': {
                        'chapter_title': 'Leprosy!'
                    },
                    '14': {
                        'chapter_title': 'Cleansing of the Leper'
                    },
                    '15': {
                        'chapter_title': 'A Holy God, A Holy People'
                    },
                    '16': {
                        'chapter_title': 'The Day of Atonement'
                    },
                    '17': {
                        'chapter_title': 'Significance of Blood'
                    },
                    '18': {
                        'chapter_title': 'How a Nation Falls -- Part 1'
                    },
                    '19': {
                        'chapter_title': 'How a Nation Falls -- Part 2'
                    },
                    '20': {
                        'chapter_title': 'How a Nation Falls -- Part 3'
                    },
                    '21': {
                        'chapter_title': 'The Walk and Work of the Priests Part 1'
                    },
                    '22': {
                        'chapter_title': 'The Walk and Work of the Priests Part 2'
                    },
                    '23': {
                        'chapter_title': 'The Feasts of the Lord'
                    },
                    '24': {
                        'chapter_title': 'Cursing and Capital Punishment'
                    },
                    '25': {
                        'chapter_title': 'The Law of the Land (The Blessing and the Curse)'
                    },
                    '26': {
                        'chapter_title': 'The Five Cycles of Discipline'
                    },
                    '27': {
                        'chapter_title': 'Vows, First-Fruits, Dedications, the Tithe'
                    }
                },
                'Numbers': {
                    'mp3': '/home/norman/Blind/recordings/numbers.mp3',
                    '1': {
                        'chapter_title': 'The Numbering of the Tribes'
                    },
                    '2': {
                        'chapter_title': 'The Arrangement of the Camp -- Part 1'
                    },
                    '3': {
                        'chapter_title': 'The Arrangement of the Camp -- Part 2'
                    },
                    '4': {
                        'chapter_title': 'The Arrangement of the Camp -- Part 3'
                    },
                    '5': {
                        'chapter_title': 'The Arrangement of the Camp -- Part 4'
                    },
                    '6': {
                        'chapter_title': 'The Arrangement of the Camp -- Part 5'
                    },
                    '7': {
                        'chapter_title': 'The Arrangement of the Camp -- Part 6'
                    },
                    '8': {
                        'chapter_title': 'The Arrangement of the Camp -- Part 7'
                    },
                    '9': {
                        'chapter_title': 'The Arrangement of the Camp -- Part 8'
                    },
                    '10': {
                        'chapter_title': 'Beginning of the March (Sinai to Kadesh Barnea)'
                    },
                    '11': {
                        'chapter_title': 'The March Continues'
                    },
                    '12': {
                        'chapter_title': 'The Murmuring of Miriam and Aaron against Moses'
                    },
                    '13': {
                        'chapter_title': 'At Kadesh -- the 12 Spies'
                    },
                    '14': {
                        'chapter_title': 'The Unbelief of Israel at Kadesh'
                    },
                    '15': {
                        'chapter_title': 'The Wandering in the Wilderness -- Part 1'
                    },
                    '16': {
                        'chapter_title': 'The Wandering in the Wilderness -- Part 2'
                    },
                    '17': {
                        'chapter_title': 'The Wandering in the Wilderness -- Part 3'
                    },
                    '18': {
                        'chapter_title': 'The Wandering in the Wilderness -- Part 4'
                    },
                    '19': {
                        'chapter_title': 'The Wandering in the Wilderness -- Part 5'
                    },
                    '20': {
                        'chapter_title': 'No Water Situation #2'
                    },
                    '21': {
                        'chapter_title': 'The Serpent of Brass'
                    },
                    '22': {
                        'chapter_title': 'Balaam and Balak -- Part 1'
                    },
                    '23': {
                        'chapter_title': 'Balaam and Balak -- Part 2'
                    },
                    '24': {
                        'chapter_title': 'Balaam and Balak -- Part 3'
                    },
                    '25': {
                        'chapter_title': 'The Doctrine of Balaam'
                    },
                    '26': {
                        'chapter_title': 'New Generation Numbered'
                    },
                    '27': {
                        'chapter_title': 'Moses Prepares to Die, Joshua Appointed'
                    },
                    '28': {
                        'chapter_title': 'Instructions on Offerings -- Part 1'
                    },
                    '29': {
                        'chapter_title': 'Instructions on Offerings -- Part 2'
                    },
                    '30': {
                        'chapter_title': 'The Law of Vows'
                    },
                    '31': {
                        'chapter_title': 'The Judgment on Midian'
                    },
                    '32': {
                        'chapter_title': 'Reuben, Gad, � Tribe of Manasseh Choose Land East of Jordan'
                    },
                    '33': {
                        'chapter_title': '40 Year Travelogue'
                    },
                    '34': {
                        'chapter_title': 'The Borders of Canaan'
                    },
                    '35': {
                        'chapter_title': 'The Cities of Refuge'
                    },
                    '36': {
                        'chapter_title': 'Inheritance Laws (Keep it in the Family)'
                    }
                },
                'Deuteronomy': {
                    'mp3': '/home/norman/Blind/recordings/deuteronomy.mp3',
                    '1': {
                        'chapter_title': 'Moses` Sermon #1 -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'Moses` Sermon #1 -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'Moses` Sermon #1 -- Part 3'
                    },
                    '4': {
                        'chapter_title': 'Moses` Sermon #2 -- Part 1'
                    },
                    '5': {
                        'chapter_title': 'Moses` Sermon #2 -- Part 2'
                    },
                    '6': {
                        'chapter_title': 'Moses` Sermon #2 -- Part 3'
                    },
                    '7': {
                        'chapter_title': 'Moses` Sermon #2 -- Part 4'
                    },
                    '8': {
                        'chapter_title': 'Moses` Sermon #2 -- Part 5'
                    },
                    '9': {
                        'chapter_title': 'Moses` Sermon #2 -- Part 6'
                    },
                    '10': {
                        'chapter_title': 'Moses` Sermon #2 -- Part 7'
                    },
                    '11': {
                        'chapter_title': 'Moses` Sermon #2 -- Part 8'
                    },
                    '12': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 1'
                    },
                    '13': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 2'
                    },
                    '14': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 3'
                    },
                    '15': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 4'
                    },
                    '16': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 5'
                    },
                    '17': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 6'
                    },
                    '18': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 7'
                    },
                    '19': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 8'
                    },
                    '20': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 9'
                    },
                    '21': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 10'
                    },
                    '22': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 11'
                    },
                    '23': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 12'
                    },
                    '24': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 13'
                    },
                    '25': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 14'
                    },
                    '26': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 15'
                    },
                    '27': {
                        'chapter_title': 'Moses` Sermon #3 -- Part 16'
                    },
                    '28': {
                        'chapter_title': 'Moses` Sermon #4 -- Part 1'
                    },
                    '29': {
                        'chapter_title': 'Moses` Sermon #4 -- Part 2'
                    },
                    '30': {
                        'chapter_title': 'Moses` Sermon #4 -- Part 3'
                    },
                    '31': {
                        'chapter_title': 'Moses` Sermon #5'
                    },
                    '32': {
                        'chapter_title': 'Moses` Song & Benediction'
                    },
                    '33': {
                        'chapter_title': 'Moses` Blessing on the Tribes'
                    },
                    '34': {
                        'chapter_title': 'Moses` Look at Canaan, Death, Burial'
                    }
                },
                'Joshua': {
                    'mp3': '/home/norman/Blind/recordings/joshua.mp3',
                    '1': {
                        'chapter_title': 'Joshua Assumes Leadership'
                    },
                    '2': {
                        'chapter_title': 'Rahab and the Spies'
                    },
                    '3': {
                        'chapter_title': 'Crossing the Jordan'
                    },
                    '4': {
                        'chapter_title': '2 Memorials (Jordan River & Gilgal)'
                    },
                    '5': {
                        'chapter_title': 'The Unseen Captain'
                    },
                    '6': {
                        'chapter_title': 'The Conquest of Jericho'
                    },
                    '7': {
                        'chapter_title': 'Defeat at Ai'
                    },
                    '8': {
                        'chapter_title': 'Victory at Ai'
                    },
                    '9': {
                        'chapter_title': 'Deception of the Gibeonites'
                    },
                    '10': {
                        'chapter_title': 'Gibeon Campaign & Southern Campaign'
                    },
                    '11': {
                        'chapter_title': 'Final Conquest of Canaan'
                    },
                    '12': {
                        'chapter_title': 'The 31 Kings'
                    },
                    '13': {
                        'chapter_title': 'Division of the Land -- Part 1'
                    },
                    '14': {
                        'chapter_title': 'Division of the Land -- Part 2'
                    },
                    '15': {
                        'chapter_title': 'Division of the Land -- Part 3'
                    },
                    '16': {
                        'chapter_title': 'Division of the Land -- Part 4'
                    },
                    '17': {
                        'chapter_title': 'Division of the Land -- Part 5'
                    },
                    '18': {
                        'chapter_title': 'The Tabernacle at Shiloh'
                    },
                    '19': {
                        'chapter_title': 'Continued Division of the Land'
                    },
                    '20': {
                        'chapter_title': 'The Cities of Refuge'
                    },
                    '21': {
                        'chapter_title': 'Continued Division of the Land (Levites)'
                    },
                    '22': {
                        'chapter_title': 'Rival, Schismatic Altar of Reuben & Gad'
                    },
                    '23': {
                        'chapter_title': 'Last Counsels of Joshua'
                    },
                    '24': {
                        'chapter_title': 'Joshua''s Death'
                    }
                },
                'Judges': {
                    'mp3': '/home/norman/Blind/recordings/judges.mp3',
                    '1': {
                        'chapter_title': '"Neither Did" Chapter'
                    },
                    '2': {
                        'chapter_title': 'Institution of the Judges'
                    },
                    '3': {
                        'chapter_title': 'Gentlemen, Start Your Engines (Judges Begin to Rule)'
                    },
                    '4': {
                        'chapter_title': 'Deborah & Barak'
                    },
                    '5': {
                        'chapter_title': 'Song of Deborah & Barak'
                    },
                    '6': {
                        'chapter_title': 'Gideon and the Fleece'
                    },
                    '7': {
                        'chapter_title': 'Gideon''s Victory, 300 Over Midian'
                    },
                    '8': {
                        'chapter_title': '1st Jealousy of Ephraim; Death of Gideon'
                    },
                    '9': {
                        'chapter_title': 'False King Abimelech'
                    },
                    '10': {
                        'chapter_title': 'The Wickedness of Israel'
                    },
                    '11': {
                        'chapter_title': 'Jephthah the 9th Judge'
                    },
                    '12': {
                        'chapter_title': '2nd Jealousy of Ephraim'
                    },
                    '13': {
                        'chapter_title': 'Samson''s Parents'
                    },
                    '14': {
                        'chapter_title': 'Samson''s Riddle'
                    },
                    '15': {
                        'chapter_title': 'Samson''s Mighty Acts'
                    },
                    '16': {
                        'chapter_title': 'Samson and Delilah'
                    },
                    '17': {
                        'chapter_title': 'The Muddle of Micah'
                    },
                    '18': {
                        'chapter_title': 'Danite Invasion & Idolatry'
                    },
                    '19': {
                        'chapter_title': 'The Levite and His Concubine'
                    },
                    '20': {
                        'chapter_title': 'Tribe of Benjamin Nearly Destroyed'
                    },
                    '21': {
                        'chapter_title': 'How to Catch a Wife'
                    }
                },
                'Ruth': {
                    'mp3': '/home/norman/Blind/recordings/ruth.mp3',
                    '1': {
                        'chapter_title': 'Ruth & Naomi Return to Judah from Moab'
                    },
                    '2': {
                        'chapter_title': 'Ruth Harvests in Boaz''s Fields'
                    },
                    '3': {
                        'chapter_title': 'Ruth and the Law of the Kinsman Redeemer'
                    },
                    '4': {
                        'chapter_title': 'Ruth Marries Boaz'
                    }
                },
                '1st Samuel': {
                    'mp3': '/home/norman/Blind/recordings/1samual.mp3',
                    '1': {
                        'chapter_title': 'Hannah and the Birth of Samuel'
                    },
                    '2': {
                        'chapter_title': 'Samuel, Eli, Eli''s Evil Sons'
                    },
                    '3': {
                        'chapter_title': 'The Call of Samuel'
                    },
                    '4': {
                        'chapter_title': 'Defeat, Ark Lost to Philistines'
                    },
                    '5': {
                        'chapter_title': 'Dagon vs. the Ark'
                    },
                    '6': {
                        'chapter_title': 'Ark Returned'
                    },
                    '7': {
                        'chapter_title': 'Ark at Home'
                    },
                    '8': {
                        'chapter_title': 'Israel Demands a King'
                    },
                    '9': {
                        'chapter_title': 'Saul Chosen'
                    },
                    '10': {
                        'chapter_title': 'Saul''s Anointing'
                    },
                    '11': {
                        'chapter_title': 'Saul''s Victory'
                    },
                    '12': {
                        'chapter_title': 'Samuel''s Valedictory Address'
                    },
                    '13': {
                        'chapter_title': 'Saul''s Rejection by God'
                    },
                    '14': {
                        'chapter_title': 'Jonathan''s Victory over the Philistines'
                    },
                    '15': {
                        'chapter_title': 'Saul''s Sheep Lie'
                    },
                    '16': {
                        'chapter_title': 'David Chosen and Anointed'
                    },
                    '17': {
                        'chapter_title': 'David & Goliath'
                    },
                    '18': {
                        'chapter_title': 'David & Jonathan'
                    },
                    '19': {
                        'chapter_title': 'David Flees from Saul'
                    },
                    '20': {
                        'chapter_title': 'Jonathan Protects David'
                    },
                    '21': {
                        'chapter_title': 'David Continues to Flee'
                    },
                    '22': {
                        'chapter_title': 'David''s Mighty Men'
                    },
                    '23': {
                        'chapter_title': 'Their Adventures'
                    },
                    '24': {
                        'chapter_title': 'David Spares Saul #1'
                    },
                    '25': {
                        'chapter_title': 'Samuel Dies'
                    },
                    '26': {
                        'chapter_title': 'David Spares Saul #2'
                    },
                    '27': {
                        'chapter_title': 'David''s Backsliding in Philistia'
                    },
                    '28': {
                        'chapter_title': 'Saul and the Witch of Endor'
                    },
                    '29': {
                        'chapter_title': 'David & Achish'
                    },
                    '30': {
                        'chapter_title': 'David and Ziklag (2 Wives Captured)'
                    },
                    '31': {
                        'chapter_title': 'The Death of Saul'
                    }
                },
                '2nd Samuel': {
                    'mp3': '/home/norman/Blind/recordings/2samual.mp3',
                    '1': {
                        'chapter_title': 'Saul & Jonathan''s Death Told to David'
                    },
                    '2': {
                        'chapter_title': 'Civil War -- Abner vs. David'
                    },
                    '3': {
                        'chapter_title': 'Civil War -- House of Saul vs. David'
                    },
                    '4': {
                        'chapter_title': 'The Murder of Ish-Bosheth'
                    },
                    '5': {
                        'chapter_title': 'David Becomes King over Israel'
                    },
                    '6': {
                        'chapter_title': 'Ark to Jerusalem'
                    },
                    '7': {
                        'chapter_title': 'The Davidic Covenant Stated'
                    },
                    '8': {
                        'chapter_title': 'David the Mighty Conqueror'
                    },
                    '9': {
                        'chapter_title': 'David & Mephibosheth'
                    },
                    '10': {
                        'chapter_title': 'The Ammonite-Syrian War'
                    },
                    '11': {
                        'chapter_title': 'David''s Sin with Bathsheba'
                    },
                    '12': {
                        'chapter_title': 'David''s Confession of Sin'
                    },
                    '13': {
                        'chapter_title': 'Amnon''s Crime (Immorality)'
                    },
                    '14': {
                        'chapter_title': 'Beautiful Absalom'
                    },
                    '15': {
                        'chapter_title': 'Absalom''s Rebellion'
                    },
                    '16': {
                        'chapter_title': 'Absalom Enters Jerusalem'
                    },
                    '17': {
                        'chapter_title': 'Absalom Listens to False Counselors'
                    },
                    '18': {
                        'chapter_title': 'Absalom Hangs by His Hair & Dies'
                    },
                    '19': {
                        'chapter_title': 'David Gets With It'
                    },
                    '20': {
                        'chapter_title': 'Sheba''s Revolt'
                    },
                    '21': {
                        'chapter_title': 'Three Years Famine'
                    },
                    '22': {
                        'chapter_title': 'David''s Son of Deliverance'
                    },
                    '23': {
                        'chapter_title': 'David''s Mighty Men'
                    },
                    '24': {
                        'chapter_title': 'David''s Numbering Sin'
                    }
                },
                '1st Kings': {
                    'mp3': '/home/norman/Blind/recordings/1kings.mp3',
                    '1': {
                        'chapter_title': 'David Failing, Solomon Anointed'
                    },
                    '2': {
                        'chapter_title': 'The Death of David'
                    },
                    '3': {
                        'chapter_title': 'Solomon''s Prayer for Wisdom'
                    },
                    '4': {
                        'chapter_title': 'Solomon Gets Wisdom'
                    },
                    '5': {
                        'chapter_title': 'Solomon''s Temple�The Building and Dedication -- Part 1'
                    },
                    '6': {
                        'chapter_title': 'Solomon''s Temple�The Building and Dedication -- Part 2'
                    },
                    '7': {
                        'chapter_title': 'Solomon''s Temple�The Building and Dedication -- Part 3'
                    },
                    '8': {
                        'chapter_title': 'Solomon''s Temple�The Building and Dedication -- Part 4'
                    },
                    '9': {
                        'chapter_title': 'Solomon''s Fame and Wealth'
                    },
                    '10': {
                        'chapter_title': 'Solomon & the Queen of Sheba'
                    },
                    '11': {
                        'chapter_title': 'The Backsliding and Death of Solomon (Rise of Jeroboam in the North)'
                    },
                    '12': {
                        'chapter_title': 'Split of the Kingdom (Rehoboam, Solomon''s Son in the South)'
                    },
                    '13': {
                        'chapter_title': 'A Wicked Jeroboam'
                    },
                    '14': {
                        'chapter_title': 'Jeroboam and Rehoboam Die'
                    },
                    '15': {
                        'chapter_title': 'Abijam, Asa, Baasha, Nabad'
                    },
                    '16': {
                        'chapter_title': 'Some of Israel''s Wicked Kings (Elah, Zimri, Tibni, Omri, Ahab)'
                    },
                    '17': {
                        'chapter_title': 'Elijah Fed by Ravens, Raising of the Widow�s Son'
                    },
                    '18': {
                        'chapter_title': 'Elijah vs. Baal (Mt. Carmel)'
                    },
                    '19': {
                        'chapter_title': 'Elijah & Still, Small Voice'
                    },
                    '20': {
                        'chapter_title': 'Ahab and Victory over Syrians'
                    },
                    '21': {
                        'chapter_title': 'Ahab, Jezebel'
                    },
                    '22': {
                        'chapter_title': 'Micaiah -- God''s Man of Conviction'
                    }
                },
                '2nd Kings': {
                    'mp3': '/home/norman/Blind/recordings/2kings.mp3',
                    '1': {
                        'chapter_title': 'Elijah -- Illness & Death of Ahaziah'
                    },
                    '2': {
                        'chapter_title': 'Elijah''s Translation'
                    },
                    '3': {
                        'chapter_title': 'Elisha -- Defeat of the Moabites'
                    },
                    '4': {
                        'chapter_title': 'Elisha''s 5 Miracle Chapter'
                    },
                    '5': {
                        'chapter_title': 'The Healing of Naaman'
                    },
                    '6': {
                        'chapter_title': 'Elisha and the Lost Axe Head'
                    },
                    '7': {
                        'chapter_title': 'Elisha: "You Will Eat!"'
                    },
                    '8': {
                        'chapter_title': 'Elisha Predicts 7 Years of Famine'
                    },
                    '9': {
                        'chapter_title': 'Jehu the Furious Driver'
                    },
                    '10': {
                        'chapter_title': 'Judgment on Ahab�s 70 Sons'
                    },
                    '11': {
                        'chapter_title': 'Only One Heir�Joash'
                    },
                    '12': {
                        'chapter_title': 'Repairing of the Temple'
                    },
                    '13': {
                        'chapter_title': 'Elisha Dies'
                    },
                    '14': {
                        'chapter_title': 'Civil War -- Israel & Judah'
                    },
                    '15': {
                        'chapter_title': 'Various Kings of Israel'
                    },
                    '16': {
                        'chapter_title': 'Rule of Ahaz'
                    },
                    '17': {
                        'chapter_title': 'Assyrian Captivity and Why'
                    },
                    '18': {
                        'chapter_title': 'Reign of Hezekiah'
                    },
                    '19': {
                        'chapter_title': 'Isaiah and Hezekiah'
                    },
                    '20': {
                        'chapter_title': 'Hezekiah''s 15 Year Extension & Death'
                    },
                    '21': {
                        'chapter_title': 'Evil King Manasseh'
                    },
                    '22': {
                        'chapter_title': 'Josiah -- Rediscovery of the Law'
                    },
                    '23': {
                        'chapter_title': 'Word Read and Passover Kept'
                    },
                    '24': {
                        'chapter_title': 'Babylon Captivity -- 70 Years'
                    },
                    '25': {
                        'chapter_title': 'Babylon Captivity -- Siege of Jerusalem'
                    }
                },
                '1st Chronicles': {
                    'mp3': '/home/norman/Blind/recordings/1chronicles.mp3',
                    '1': {
                        'chapter_title': 'Genealogies -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'Genealogies -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'Genealogies -- Part 3'
                    },
                    '4': {
                        'chapter_title': 'Genealogies -- Part 4'
                    },
                    '5': {
                        'chapter_title': 'Genealogies -- Part 5'
                    },
                    '6': {
                        'chapter_title': 'Genealogies -- Part 6'
                    },
                    '7': {
                        'chapter_title': 'Genealogies -- Part 7'
                    },
                    '8': {
                        'chapter_title': 'Genealogies -- Part 8'
                    },
                    '9': {
                        'chapter_title': 'Genealogies -- Part 9'
                    },
                    '10': {
                        'chapter_title': 'Saul''s Death'
                    },
                    '11': {
                        'chapter_title': 'David''s Mighty Men -- Part 1'
                    },
                    '12': {
                        'chapter_title': 'David''s Mighty Men -- Part 2'
                    },
                    '13': {
                        'chapter_title': 'Uzza and the Ark'
                    },
                    '14': {
                        'chapter_title': 'David and the Mulberry Trees'
                    },
                    '15': {
                        'chapter_title': 'Ark Returned'
                    },
                    '16': {
                        'chapter_title': 'David and a Psalm'
                    },
                    '17': {
                        'chapter_title': 'The Davidic Covenant'
                    },
                    '18': {
                        'chapter_title': 'David''s Mighty Kingdom (then)'
                    },
                    '19': {
                        'chapter_title': 'The Ammonite-Syrian War'
                    },
                    '20': {
                        'chapter_title': 'The Giant with 24 Fingers and Toes'
                    },
                    '21': {
                        'chapter_title': 'David''s Numbering Sin'
                    },
                    '22': {
                        'chapter_title': 'David Prepares Materials for the Temp'
                    },
                    '23': {
                        'chapter_title': 'Solomon Made King, Organization of Levitical Priests'
                    },
                    '24': {
                        'chapter_title': 'Organization of Israel Continued -- Part 1'
                    },
                    '25': {
                        'chapter_title': 'Organization of Israel Continued -- Part 2'
                    },
                    '26': {
                        'chapter_title': 'Organization of Israel Continued -- Part 3'
                    },
                    '27': {
                        'chapter_title': 'Organization of Israel Continued -- Part 4'
                    },
                    '28': {
                        'chapter_title': 'Closing Counsel of David, Teenage Solomon Reigns, David Dies -- Part 1'
                    },
                    '29': {
                        'chapter_title': 'Closing Counsel of David, Teenage Solomon Reigns, David Dies -- Part 2'
                    }
                },
                '2nd Chronicles':
                {
                    'mp3': '/home/norman/Blind/recordings/2chronicles.mp3',
                    '1': {
                        'chapter_title': 'Solomon and His Wisdom'
                    },
                    '2': {
                        'chapter_title': 'Solomon Builds the Temple -- Part 1'
                    },
                    '3': {
                        'chapter_title': 'Solomon Builds the Temple -- Part 2'
                    },
                    '4': {
                        'chapter_title': 'Solomon Builds the Temple -- Part 3'
                    },
                    '5': {
                        'chapter_title': 'Ark Put in Temple, Glory Fills the Temple'
                    },
                    '6': {
                        'chapter_title': 'Solomon Dedicates the Temple'
                    },
                    '7': {
                        'chapter_title': 'The Lord is Pleased'
                    },
                    '8': {
                        'chapter_title': 'Solomon''s Activity and Wealth'
                    },
                    '9': {
                        'chapter_title': 'Solomon and the Queen of Sheba'
                    },
                    '10': {
                        'chapter_title': 'Rehoboam Over 2 Southern Tribes -- Part 1'
                    },
                    '11': {
                        'chapter_title': 'Rehoboam Over 2 Southern Tribes -- Part 2'
                    },
                    '12': {
                        'chapter_title': 'Rehoboam Over 2 Southern Tribes -- Part 3'
                    },
                    '13': {
                        'chapter_title': 'Jeroboam Over 10 Northern Tribes'
                    },
                    '14': {
                        'chapter_title': 'Good King Asa -- Part 1'
                    },
                    '15': {
                        'chapter_title': 'Good King Asa -- Part 2'
                    },
                    '16': {
                        'chapter_title': 'Good King Asa -- Part 3'
                    },
                    '17': {
                        'chapter_title': 'Good King Jehoshaphat (note unholy alliance with Ahab) -- Part 1'
                    },
                    '18': {
                        'chapter_title': 'Good King Jehoshaphat (note unholy alliance with Ahab) -- Part 2'
                    },
                    '19': {
                        'chapter_title': 'Good King Jehoshaphat (note unholy alliance with Ahab) -- Part 3'
                    },
                    '20': {
                        'chapter_title': 'Good King Jehoshaphat (note unholy alliance with Ahab) -- Part 4'
                    },
                    '21': {
                        'chapter_title': 'Jehoram''s Reign [J]'
                    },
                    '22': {
                        'chapter_title': 'Only One Heir Left in the Royal Line of Christ, Joash'
                    },
                    '23': {
                        'chapter_title': 'Reign of Joash [J] -- Part 1'
                    },
                    '24': {
                        'chapter_title': 'Reign of Joash [J] -- Part 2'
                    },
                    '25': {
                        'chapter_title': 'Reign of Amaziah [J]'
                    },
                    '26': {
                        'chapter_title': 'Reign of Uzziah [J]'
                    },
                    '27': {
                        'chapter_title': 'Reign of Jothan [J]'
                    },
                    '28': {
                        'chapter_title': 'Reign of Ahaz [J]'
                    },
                    '29': {
                        'chapter_title': 'Reign of Hezekiah [J] -- Part 1'
                    },
                    '30': {
                        'chapter_title': 'Reign of Hezekiah [J] -- Part 2'
                    },
                    '31': {
                        'chapter_title': 'Reign of Hezekiah [J] -- Part 3'
                    },
                    '32': {
                        'chapter_title': 'Reign of Hezekiah [J] -- Part 4'
                    },
                    '33': {
                        'chapter_title': 'Reign of Manasseh (55) [J]'
                    },
                    '34': {
                        'chapter_title': 'Reign of Josiah [J] -- Part 1'
                    },
                    '35': {
                        'chapter_title': 'Reign of Josiah [J] -- Part 2'
                    },
                    '36': {
                        'chapter_title': 'The Babylonian Captivity'
                    }
                },
                'Ezra': {
                    'mp3': '/home/norman/Blind/recordings/ezra.mp3',
                    '1': {
                        'chapter_title': 'Decree of Cyrus (Restoration of the Temple)'
                    },
                    '2': {
                        'chapter_title': 'The Returning Remnant'
                    },
                    '3': {
                        'chapter_title': 'Temple Foundations Laid'
                    },
                    '4': {
                        'chapter_title': 'Opposition, Letter to Artaxerxes, Work Stopped'
                    },
                    '5': {
                        'chapter_title': 'Opposition Answered'
                    },
                    '6': {
                        'chapter_title': 'Decree of Darius (Temple Finished)'
                    },
                    '7': {
                        'chapter_title': 'Ezra Thanks the Lord'
                    },
                    '8': {
                        'chapter_title': 'Treasure Brought to the Temp'
                    },
                    '9': {
                        'chapter_title': 'Unholy (Mixed) Marriages, Ezra''s Prayer'
                    },
                    '10': {
                        'chapter_title': 'The Above Sin is Judged and Restitution Made'
                    }
                },
                'Nehemiah': {
                    'mp3': '/home/norman/Blind/recordings/nehemiah.mp3',
                    '1': {
                        'chapter_title': 'The Ruined Walls'
                    },
                    '2': {
                        'chapter_title': 'Nehemiah Surveys the Ruins'
                    },
                    '3': {
                        'chapter_title': 'The Builders Begin to Build'
                    },
                    '4': {
                        'chapter_title': 'Opposition in the Rebuilding -- Part 1'
                    },
                    '5': {
                        'chapter_title': 'Opposition in the Rebuilding -- Part 2'
                    },
                    '6': {
                        'chapter_title': 'Opposition in the Rebuilding -- Part 3'
                    },
                    '7': {
                        'chapter_title': 'Genealogies'
                    },
                    '8': {
                        'chapter_title': 'Ezra’s Expository Preaching'
                    },
                    '9': {
                        'chapter_title': 'Review of Old Testament History'
                    },
                    '10': {
                        'chapter_title': 'Application of Teaching to Experience'
                    },
                    '11': {
                        'chapter_title': 'Geographical Distribution of the Inhabitants of Israel'
                    },
                    '12': {
                        'chapter_title': 'Dedication of the Walls'
                    },
                    '13': {
                        'chapter_title': 'The Law and Separation'
                    }
                },
                'Esther': {
                    'mp3': '/home/norman/Blind/recordings/esther.mp3',
                    '1': {
                        'chapter_title': 'Queen Vashti Disobeys the King'
                    },
                    '2': {
                        'chapter_title': 'Queen Esther the Jew'
                    },
                    '3': {
                        'chapter_title': 'Mordecai and Haman'
                    },
                    '4': {
                        'chapter_title': 'Planned Extermination of the Jewish Nation'
                    },
                    '5': {
                        'chapter_title': '“If I Perish, I Perish”'
                    },
                    '6': {
                        'chapter_title': 'Haman Shamed'
                    },
                    '7': {
                        'chapter_title': 'Haman Hanged'
                    },
                    '8': {
                        'chapter_title': 'The Jews Delivered'
                    },
                    '9': {
                        'chapter_title': 'The Feast of Purim (Celebrating Jewish Deliverance)'
                    },
                    '10': {
                        'chapter_title': 'Mordecai, #2 in the Kingdom'
                    }
                },
                'Job': {
                    'mp3': '/home/norman/Blind/recordings/job.mp3',
                    '1': {
                        'chapter_title': 'Job and Suffering (Family)'
                    },
                    '2': {
                        'chapter_title': 'Job and Suffering (Personal) -- Part 1'
                    },
                    '3': {
                        'chapter_title': 'Job and Suffering (Personal) -- Part 2'
                    },
                    '4': {
                        'chapter_title': 'Eliphaz’s First Prosecution -- Part 1'
                    },
                    '5': {
                        'chapter_title': 'Eliphaz’s First Prosecution -- Part 2'
                    },
                    '6': {
                        'chapter_title': 'Job’s Defense -- Part 1'
                    },
                    '7': {
                        'chapter_title': 'Job’s Defense -- Part 2'
                    },
                    '8': {
                        'chapter_title': 'Bildad’s First Prosecution'
                    },
                    '9': {
                        'chapter_title': 'Job’s Defense -- Part 1'
                    },
                    '10': {
                        'chapter_title': 'Job’s Defense -- Part 2'
                    },
                    '11': {
                        'chapter_title': 'Zophar’s First Prosecution'
                    },
                    '12': {
                        'chapter_title': 'Job’s Defense -- Part 1'
                    },
                    '13': {
                        'chapter_title': 'Job’s Defense -- Part 2'
                    },
                    '14': {
                        'chapter_title': 'Job’s Defense -- Part 3'
                    },
                    '15': {
                        'chapter_title': 'Eliphaz’s Second Prosecution'
                    },
                    '16': {
                        'chapter_title': 'Job’s Defense -- Part 1'
                    },
                    '17': {
                        'chapter_title': 'Job’s Defense -- Part 2'
                    },
                    '18': {
                        'chapter_title': 'Bildad’s Second Prosecution'
                    },
                    '19': {
                        'chapter_title': 'Job’s Defense'
                    },
                    '20': {
                        'chapter_title': 'Zophar’s Final Arguments'
                    },
                    '21': {
                        'chapter_title': 'Job’s Defense'
                    },
                    '22': {
                        'chapter_title': 'Eliphaz’s Final Arguments'
                    },
                    '23': {
                        'chapter_title': 'Job’s Defense -- Part 1'
                    },
                    '24': {
                        'chapter_title': 'Job’s Defense -- Part 2'
                    },
                    '25': {
                        'chapter_title': 'Bildad’s Final Arguments'
                    },
                    '26': {
                        'chapter_title': 'Job’s Defense -- Part 1'
                    },
                    '27': {
                        'chapter_title': 'Job’s Defense -- Part 2'
                    },
                    '28': {
                        'chapter_title': 'Job’s Defense -- Part 3'
                    },
                    '29': {
                        'chapter_title': 'Job’s Defense -- Part 4'
                    },
                    '30': {
                        'chapter_title': 'Job’s Defense -- Part 5'
                    },
                    '31': {
                        'chapter_title': 'Job’s Defense -- Part 6'
                    },
                    '32': {
                        'chapter_title': 'The Speech of Elihu -- Part 1'
                    },
                    '33': {
                        'chapter_title': 'The Speech of Elihu -- Part 2'
                    },
                    '34': {
                        'chapter_title': 'The Speech of Elihu -- Part 3'
                    },
                    '35': {
                        'chapter_title': 'The Speech of Elihu -- Part 4'
                    },
                    '36': {
                        'chapter_title': 'The Speech of Elihu -- Part 5'
                    },
                    '37': {
                        'chapter_title': 'The Speech of Elihu -- Part 6'
                    },
                    '38': {
                        'chapter_title': 'God Talks to Job -- Part 1'
                    },
                    '39': {
                        'chapter_title': 'God Talks to Job -- Part 2'
                    },
                    '40': {
                        'chapter_title': 'God Talks to Job -- Part 3'
                    },
                    '41': {
                        'chapter_title': 'God Talks to Job -- Part 4'
                    },
                    '42': {
                        'chapter_title': 'Job’s Confessions & Restoration'
                    }
                },
                'Psalms': {
                    'mp3': '/home/norman/Blind/recordings/psalms.mp3',
                    '1': {
                        'chapter_title': 'The Blessed Man'
                    },
                    '2': {
                        'chapter_title': 'The King Rejected but Coming to Reign'
                    },
                    '3': {
                        'chapter_title': 'A Psalm in Distress'
                    },
                    '4': {
                        'chapter_title': 'Prayer in Trouble'
                    },
                    '5': {
                        'chapter_title': 'Sharing God’s Attitude Toward Sin'
                    },
                    '6': {
                        'chapter_title': 'Praying in Deepest Distress'
                    },
                    '7': {
                        'chapter_title': 'The Slandered Saint Psalm'
                    },
                    '8': {
                        'chapter_title': 'The Son of Man Reigning'
                    },
                    '9': {
                        'chapter_title': 'Praise for Righteous Judgment'
                    },
                    '10': {
                        'chapter_title': 'A Psalm Concerning the Wicked'
                    },
                    '11': {
                        'chapter_title': 'The Psalm of the Steadfast'
                    },
                    '12': {
                        'chapter_title': 'Liars Against the Truth'
                    },
                    '13': {
                        'chapter_title': 'The “How Long” Psalm'
                    },
                    '14': {
                        'chapter_title': 'The Psalm of the Fool'
                    },
                    '15': {
                        'chapter_title': 'The Regenerate Described'
                    },
                    '16': {
                        'chapter_title': 'Death and Resurrection'
                    },
                    '17': {
                        'chapter_title': 'A Prayer of David Against the Wicked'
                    },
                    '18': {
                        'chapter_title': 'David’s Psalm of Deliverance'
                    },
                    '19': {
                        'chapter_title': 'The Witness of Creation and Revelation'
                    },
                    '20': {
                        'chapter_title': 'A Psalm for a Day of Trouble'
                    },
                    '21': {
                        'chapter_title': 'Victorious King Psalm'
                    },
                    '22': {
                        'chapter_title': 'The Good Shepherd (Crucified)'
                    },
                    '23': {
                        'chapter_title': 'The Great Shepherd (Risen)'
                    },
                    '24': {
                        'chapter_title': 'The Chief Shepherd (Coming)'
                    },
                    '25': {
                        'chapter_title': 'Trust in the Midst of Trouble'
                    },
                    '26': {
                        'chapter_title': 'How to Avoid Backsliding'
                    },
                    '27': {
                        'chapter_title': 'One Desire in Time of Trouble'
                    },
                    '28': {
                        'chapter_title': 'A Cry for Judgment'
                    },
                    '29': {
                        'chapter_title': 'The Judgment Storm'
                    },
                    '30': {
                        'chapter_title': 'A Psalm of Dedication'
                    },
                    '31': {
                        'chapter_title': 'A Psalm of Trouble and Trust'
                    },
                    '32': {
                        'chapter_title': 'David’s Testimony of Confession'
                    },
                    '33': {
                        'chapter_title': 'Praise for Creation, Providence, Grace'
                    },
                    '34': {
                        'chapter_title': 'Appreciation for Deliverance'
                    },
                    '35': {
                        'chapter_title': 'A Prayer for Intercessors'
                    },
                    '36': {
                        'chapter_title': 'Wicked Way and God’s Way Contrasted'
                    },
                    '37': {
                        'chapter_title': '“Fret Not” Psalm'
                    },
                    '38': {
                        'chapter_title': 'David, Out of Fellowship, In at End'
                    },
                    '39': {
                        'chapter_title': 'Prayer for Wisdom'
                    },
                    '40': {
                        'chapter_title': 'The Obedience of Christ, New Song'
                    },
                    '41': {
                        'chapter_title': 'Prophesied Betrayal by Judas'
                    },
                    '42': {
                        'chapter_title': '“Hope Thou in God” Psalm'
                    },
                    '43': {
                        'chapter_title': 'Enemies Bug Me'
                    },
                    '44': {
                        'chapter_title': 'Undeserved Suffering'
                    },
                    '45': {
                        'chapter_title': 'Royal Wedding Psalm'
                    },
                    '46': {
                        'chapter_title': 'Triumph in the Great Tribulation Period'
                    },
                    '47': {
                        'chapter_title': 'The Lord Reigning'
                    },
                    '48': {
                        'chapter_title': 'Jerusalem'
                    },
                    '49': {
                        'chapter_title': 'The Folly of Unbelief'
                    },
                    '50': {
                        'chapter_title': 'The Nature of True Worship'
                    },
                    '51': {
                        'chapter_title': 'David’s Sin Acknowledged'
                    },
                    '52': {
                        'chapter_title': '“Green Olive Tree” Psalm'
                    },
                    '53': {
                        'chapter_title': 'The Psalm of the Fool (Same as Psalm 14)'
                    },
                    '54': {
                        'chapter_title': '“Mine Helper” Psalm'
                    },
                    '55': {
                        'chapter_title': 'Escape From Tribulation'
                    },
                    '56': {
                        'chapter_title': 'A Prayer of the Hunted One'
                    },
                    '57': {
                        'chapter_title': 'Refuge in Trouble'
                    },
                    '58': {
                        'chapter_title': 'Imprecatory Psalm'
                    },
                    '59': {
                        'chapter_title': 'Prayer for Deliverance and Judgment'
                    },
                    '60': {
                        'chapter_title': 'Through Defeat to Victory'
                    },
                    '61': {
                        'chapter_title': 'Refuge in the Rock'
                    },
                    '62': {
                        'chapter_title': 'Confidence in God the Rock'
                    },
                    '63': {
                        'chapter_title': '“Most Beautiful” Psalm'
                    },
                    '64': {
                        'chapter_title': 'Wicked vs. the Righteous'
                    },
                    '65': {
                        'chapter_title': 'Thanksgiving Psalm'
                    },
                    '66': {
                        'chapter_title': 'Worthy Worship Psalm'
                    },
                    '67': {
                        'chapter_title': 'Future Kingdom Blessing'
                    },
                    '68': {
                        'chapter_title': 'Victorious Procession of God'
                    },
                    '69': {
                        'chapter_title': 'The Sufferings of Christ'
                    },
                    '70': {
                        'chapter_title': 'Memorial Psalm'
                    },
                    '71': {
                        'chapter_title': 'Aged Saint Psalm'
                    },
                    '72': {
                        'chapter_title': 'King and the Kingdom'
                    },
                    '73': {
                        'chapter_title': 'Envious at the Prosperity of the Wicked'
                    },
                    '74': {
                        'chapter_title': 'The Enemy in Possession'
                    },
                    '75': {
                        'chapter_title': 'The Lord’s Cup of Judgment'
                    },
                    '76': {
                        'chapter_title': 'When God Reigns in Zion'
                    },
                    '77': {
                        'chapter_title': 'The Troubled Saint'
                    },
                    '78': {
                        'chapter_title': 'The History of God’s Grace With Israel'
                    },
                    '79': {
                        'chapter_title': 'A Prayer With Jerusalem in Ruins!'
                    },
                    '80': {
                        'chapter_title': 'Christ, the Strong Man'
                    },
                    '81': {
                        'chapter_title': 'God Bares the Heart'
                    },
                    '82': {
                        'chapter_title': 'God is the Judge'
                    },
                    '83': {
                        'chapter_title': 'Afflicted to Learn!'
                    },
                    '84': {
                        'chapter_title': '“Sons of Grace” Psalm'
                    },
                    '85': {
                        'chapter_title': '“Revival Prayer” Psalm'
                    },
                    '86': {
                        'chapter_title': 'Poor and Needy Prayer'
                    },
                    '87': {
                        'chapter_title': 'A Song of Zion'
                    },
                    '88': {
                        'chapter_title': '“Deepest Distress” Psalm'
                    },
                    '89': {
                        'chapter_title': '“Davidic Covenant” Psalm'
                    },
                    '90': {
                        'chapter_title': 'The Psalm of Death (First Adam)'
                    },
                    '91': {
                        'chapter_title': 'The Psalm of Life (Last Adam)'
                    },
                    '92': {
                        'chapter_title': 'Sabbath Palm (of rest)'
                    },
                    '93': {
                        'chapter_title': 'The King and His Throne'
                    },
                    '94': {
                        'chapter_title': 'A Prayer for Vengeance'
                    },
                    '95': {
                        'chapter_title': 'A Psalm of Praise and Warning'
                    },
                    '96': {
                        'chapter_title': 'Praise and Testimony in View of the Second Advent'
                    },
                    '97': {
                        'chapter_title': '“The Lord Reigneth” Psalm'
                    },
                    '98': {
                        'chapter_title': 'A New Song of Victory'
                    },
                    '99': {
                        'chapter_title': 'Righteous Judgment & Trembling'
                    },
                    '100': {
                        'chapter_title': 'The Old Hundreth (Thanksgiving)'
                    },
                    '101': {
                        'chapter_title': 'The King and His Subjects'
                    },
                    '102': {
                        'chapter_title': 'A Prayer in Humiliation'
                    },
                    '103': {
                        'chapter_title': '“Bless the Lord, O My Soul” Psalm'
                    },
                    '104': {
                        'chapter_title': 'The Praise of His Works'
                    },
                    '105': {
                        'chapter_title': 'Israel’s History & God’s Mercy'
                    },
                    '106': {
                        'chapter_title': 'Israel’s Failure & God’s Grace'
                    },
                    '107': {
                        'chapter_title': 'Thanksgiving for Affliction'
                    },
                    '108': {
                        'chapter_title': 'Praise for Victory'
                    },
                    '109': {
                        'chapter_title': '“Satanic Power” Psalm'
                    },
                    '110': {
                        'chapter_title': 'Christ as King and Priest'
                    },
                    '111': {
                        'chapter_title': '“Reverend is His Name” Psalm'
                    },
                    '112': {
                        'chapter_title': 'God’s Plan is Greater than the Pressures of Life'
                    },
                    '113': {
                        'chapter_title': 'From Dunghill to Ruler'
                    },
                    '114': {
                        'chapter_title': 'When Israel Went Out of Egypt'
                    },
                    '115': {
                        'chapter_title': 'God Compared With Idols'
                    },
                    '116': {
                        'chapter_title': '“Dying Grace” Psalm'
                    },
                    '117': {
                        'chapter_title': 'The Shortest Psalm (praise)'
                    },
                    '118': {
                        'chapter_title': 'The Exalted Christ'
                    },
                    '119': {
                        'chapter_title': '“The Word of God” Psalm'
                    },
                    '120': {
                        'chapter_title': 'Prayer Against a Lying Tongue'
                    },
                    '121': {
                        'chapter_title': 'The Traveler’s Psalm'
                    },
                    '122': {
                        'chapter_title': 'Jerusalem and Peace'
                    },
                    '123': {
                        'chapter_title': 'Waiting in Faith'
                    },
                    '124': {
                        'chapter_title': 'Lord on our Side'
                    },
                    '125': {
                        'chapter_title': 'Security for the Trusting'
                    },
                    '126': {
                        'chapter_title': 'A Psalm of Freedom'
                    },
                    '127': {
                        'chapter_title': 'Safety in the Lord'
                    },
                    '128': {
                        'chapter_title': 'Earthly Blessings'
                    },
                    '129': {
                        'chapter_title': 'Comfort in Affliction'
                    },
                    '130': {
                        'chapter_title': 'Who Shall Stand?'
                    },
                    '131': {
                        'chapter_title': 'Childlike Trust'
                    },
                    '132': {
                        'chapter_title': 'Davidic Covenant Psalm'
                    },
                    '133': {
                        'chapter_title': 'A Psalm of Fellowship'
                    },
                    '134': {
                        'chapter_title': 'Worship at Night'
                    },
                    '135': {
                        'chapter_title': 'Priestly Praise Psalm'
                    },
                    '136': {
                        'chapter_title': 'His Mercy Endureth Forever'
                    },
                    '137': {
                        'chapter_title': 'Babylon Captivity Weeping'
                    },
                    '138': {
                        'chapter_title': '“Magnified Thy Word Above Thy Name” Psalm'
                    },
                    '139': {
                        'chapter_title': 'Spiritual Life Psalm'
                    },
                    '140': {
                        'chapter_title': 'Opposition from Evil'
                    },
                    '141': {
                        'chapter_title': '“Guard My Speech” Psalm'
                    },
                    '142': {
                        'chapter_title': 'The Prisoner’s Psalm'
                    },
                    '143': {
                        'chapter_title': 'A Prayer for Mercy in Persecution'
                    },
                    '144': {
                        'chapter_title': 'Military Strength Psalm'
                    },
                    '145': {
                        'chapter_title': 'Pure Praise Psalm'
                    },
                    '146': {
                        'chapter_title': 'Praise and Trust'
                    },
                    '147': {
                        'chapter_title': 'Praise for God’s Grace to Israel'
                    },
                    '148': {
                        'chapter_title': 'Praise from all Creation'
                    },
                    '149': {
                        'chapter_title': 'A New Song of Praise'
                    },
                    '150': {
                        'chapter_title': 'Praise Ye the Lord'
                    }
                },
                'Proverbs': {
                    'mp3': '/home/norman/Blind/recordings/proverbs.mp3',
                    '1': {
                        'chapter_title': 'Introduction to Wisdom'
                    },
                    '2': {
                        'chapter_title': 'Seek Bible Doctrine Wholeheartedly'
                    },
                    '3': {
                        'chapter_title': 'Elaboration on Bible Doctrine -- Part 1'
                    },
                    '4': {
                        'chapter_title': 'Elaboration on Bible Doctrine -- Part 2'
                    },
                    '5': {
                        'chapter_title': 'Illegitimate Love Condemned -- Part 1'
                    },
                    '6': {
                        'chapter_title': 'Illegitimate Love Condemned -- Part 2'
                    },
                    '7': {
                        'chapter_title': 'Illegitimate Love Condemned -- Part 3'
                    },
                    '8': {
                        'chapter_title': 'Good Women vs. Bad Women -- Part 1'
                    },
                    '9': {
                        'chapter_title': 'Good Women vs. Bad Women -- Part 2'
                    },
                    '10': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 1'
                    },
                    '11': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 2'
                    },
                    '12': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 3'
                    },
                    '13': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 4'
                    },
                    '14': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 5'
                    },
                    '15': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 6'
                    },
                    '16': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 7'
                    },
                    '17': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 8'
                    },
                    '18': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 9'
                    },
                    '19': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 10'
                    },
                    '20': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 11'
                    },
                    '21': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 12'
                    },
                    '22': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 13'
                    },
                    '23': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 14'
                    },
                    '24': {
                        'chapter_title': 'Application of Bible Doctrine to Experience -- Part 15'
                    },
                    '25': {
                        'chapter_title': 'Proverbs Concerning the Fool -- Part 1'
                    },
                    '26': {
                        'chapter_title': 'Proverbs Concerning the Fool -- Part 2'
                    },
                    '27': {
                        'chapter_title': 'Proverbs Concerning the Fool -- Part 3'
                    },
                    '28': {
                        'chapter_title': 'Proverbs Concerning the Fool -- Part 4'
                    },
                    '29': {
                        'chapter_title': 'Proverbs Concerning the Fool -- Part 5'
                    },
                    '30': {
                        'chapter_title': 'Words of Agur'
                    },
                    '31': {
                        'chapter_title': 'A Virtuous Woman'
                    }
                },
                'Ecclesiastes': {
                    'mp3': '/home/norman/Blind/recordings/ecclesiastes.mp3',
                    '1': {
                        'chapter_title': 'Nothing Satisfies the Carnal Believer'
                    },
                    '2': {
                        'chapter_title': 'Pleasures & Materialism Do Not Satisfy'
                    },
                    '3': {
                        'chapter_title': 'Egotism Does Not Satisfy -- Part 1'
                    },
                    '4': {
                        'chapter_title': 'Egotism Does Not Satisfy -- Part 2'
                    },
                    '5': {
                        'chapter_title': 'Empty Religion and Wealth Do Not Satisfy -- Part 1'
                    },
                    '6': {
                        'chapter_title': 'Empty Religion and Wealth Do Not Satisfy -- Part 2'
                    },
                    '7': {
                        'chapter_title': 'Humanitarian Works Do Not Satisfy -- Part 1'
                    },
                    '8': {
                        'chapter_title': 'Humanitarian Works Do Not Satisfy -- Part 2'
                    },
                    '9': {
                        'chapter_title': 'Humanitarian Works Do Not Satisfy -- Part 3'
                    },
                    '10': {
                        'chapter_title': 'Humanitarian Works Do Not Satisfy -- Part 4'
                    },
                    '11': {
                        'chapter_title': 'Humanitarian Works Do Not Satisfy -- Part 5'
                    },
                    '12': {
                        'chapter_title': 'Get Back in Fellowship & Walk with the Lord -- Part 1'
                    },
                    '13': {
                        'chapter_title': 'Get Back in Fellowship & Walk with the Lord -- Part 2'
                    },
                    '14': {
                        'chapter_title': 'Get Back in Fellowship & Walk with the Lord -- Part 3'
                    }
                },
                'Song of Solomon': {
                    '1': {
                        'chapter_title': 'Conversation Between Shulamite Woman and the Daughters of Jerusalem'
                    },
                    '2': {
                        'chapter_title': 'The Shulamite’s Thoughts of Her Shepherd Lover'
                    },
                    '3': {
                        'chapter_title': 'The Woman’s Search for Her Lover, Her Desire to Marry Him, Glimpse of Rival Lover Solomon in all His Glory.'
                    },
                    '4': {
                        'chapter_title': 'The Wooing of King Solomon, She Says No'
                    },
                    '5': {
                        'chapter_title': 'The Woman’s Thoughts Concerning Her Shepherd Lover'
                    },
                    '6': {
                        'chapter_title': 'Solomon Woos, She Refuses'
                    },
                    '7': {
                        'chapter_title': 'The Shulamite Woman Escapes'
                    },
                    '8': {
                        'chapter_title': 'Shulamite Lover and Shepherd Lover Together Again in their Home Town.'
                    }
                },
                'Isaiah': {
                    '1': {
                        'chapter_title': 'Terrible Wickedness of Judah'
                    },
                    '2': {
                        'chapter_title': 'Preview of the Millennial Age -- Part 1'
                    },
                    '3': {
                        'chapter_title': 'Preview of the Millennial Age -- Part 2'
                    },
                    '4': {
                        'chapter_title': 'Preview of the Millennial Age -- Part 3'
                    },
                    '5': {
                        'chapter_title': 'Vineyard Funeral Dirge'
                    },
                    '6': {
                        'chapter_title': 'The Call of Isaiah'
                    },
                    '7': {
                        'chapter_title': 'The Virgin Birth Chapter'
                    },
                    '8': {
                        'chapter_title': 'Maher-shalal-hash-baz'
                    },
                    '9': {
                        'chapter_title': 'Names of Christ Prophesied'
                    },
                    '10': {
                        'chapter_title': 'The Advancing Assyrians'
                    },
                    '11': {
                        'chapter_title': 'The Branch and Millennial Kingdom -- Part 1'
                    },
                    '12': {
                        'chapter_title': 'The Branch and Millennial Kingdom -- Part 2'
                    },
                    '13': {
                        'chapter_title': 'Fall of Babylon & Philistia -- Part 1'
                    },
                    '14': {
                        'chapter_title': 'Fall of Babylon & Philistia -- Part 2'
                    },
                    '15': {
                        'chapter_title': 'Moab -- Part 1'
                    },
                    '16': {
                        'chapter_title': 'Moab -- Part 2'
                    },
                    '17': {
                        'chapter_title': 'Damascus'
                    },
                    '18': {
                        'chapter_title': 'Ethiopia'
                    },
                    '19': {
                        'chapter_title': 'Egypt'
                    },
                    '20': {
                        'chapter_title': 'Egypt and Ethiopia, Babylon, Edom, Arabia -- Part 1'
                    },
                    '21': {
                        'chapter_title': 'Egypt and Ethiopia, Babylon, Edom, Arabia -- Part 2'
                    },
                    '22': {
                        'chapter_title': 'Jerusalem'
                    },
                    '23': {
                        'chapter_title': 'Tyre'
                    },
                    '24': {
                        'chapter_title': 'Tribulational Troubles'
                    },
                    '25': {
                        'chapter_title': 'Millennial Mercies'
                    },
                    '26': {
                        'chapter_title': '“Thou Wilt Keep Him in Perfect Peace”'
                    },
                    '27': {
                        'chapter_title': 'Israel Regathered'
                    },
                    '28': {
                        'chapter_title': 'Denouncing Samaria and Jerusalem'
                    },
                    '29': {
                        'chapter_title': 'Imminent Siege of Jerusalem'
                    },
                    '30': {
                        'chapter_title': 'Judah’s Alliance With Egypt -- Part 1'
                    },
                    '31': {
                        'chapter_title': 'Judah’s Alliance With Egypt -- Part 2'
                    },
                    '32': {
                        'chapter_title': 'Preparation for Armageddon -- Part 1'
                    },
                    '33': {
                        'chapter_title': 'Preparation for Armageddon -- Part 2'
                    },
                    '34': {
                        'chapter_title': 'Preparation for Armageddon -- Part 3'
                    },
                    '35': {
                        'chapter_title': 'The Regathering of Israel (2nd Advent)'
                    },
                    '36': {
                        'chapter_title': 'Assyrian Army Defeated -- Part 1'
                    },
                    '37': {
                        'chapter_title': 'Assyrian Army Defeated -- Part 2'
                    },
                    '38': {
                        'chapter_title': 'Hezekiah’s Sickness and Death -- Part 1'
                    },
                    '39': {
                        'chapter_title': 'Hezekiah’s Sickness and Death -- Part 2'
                    },
                    '40': {
                        'chapter_title': 'Words of Comfort -- Part 1'
                    },
                    '41': {
                        'chapter_title': 'Words of Comfort -- Part 2'
                    },
                    '42': {
                        'chapter_title': 'Words of Comfort -- Part 3'
                    },
                    '43': {
                        'chapter_title': 'Words of Comfort -- Part 4'
                    },
                    '44': {
                        'chapter_title': 'Words of Comfort -- Part 5'
                    },
                    '45': {
                        'chapter_title': 'Prophecy of Cyrus'
                    },
                    '46': {
                        'chapter_title': 'Fall of Babylon -- Part 1'
                    },
                    '47': {
                        'chapter_title': 'Fall of Babylon -- Part 2'
                    },
                    '48': {
                        'chapter_title': 'Fall of Babylon -- Part 3'
                    },
                    '49': {
                        'chapter_title': 'The Great Deliverer—God -- Part 1'
                    },
                    '50': {
                        'chapter_title': 'The Great Deliverer—God -- Part 2'
                    },
                    '51': {
                        'chapter_title': 'The Great Deliverer—God -- Part 3'
                    },
                    '52': {
                        'chapter_title': 'The Great Deliverer—God -- Part 4'
                    },
                    '53': {
                        'chapter_title': 'The Great Deliverer—God -- Part 5'
                    },
                    '54': {
                        'chapter_title': 'The Great Deliverer—God -- Part 6'
                    },
                    '55': {
                        'chapter_title': 'The Great Deliverer—God -- Part 7'
                    },
                    '56': {
                        'chapter_title': 'The Great Deliverer—God -- Part 8'
                    },
                    '57': {
                        'chapter_title': 'The Great Deliverer—God -- Part 9'
                    },
                    '58': {
                        'chapter_title': 'Comparison of the Faithful and Unfaithful -- Part 1'
                    },
                    '59': {
                        'chapter_title': 'Comparison of the Faithful and Unfaithful -- Part 2'
                    },
                    '60': {
                        'chapter_title': 'The Glorious Redeemer, Jerusalem & its Citizens -- Part 1'
                    },
                    '61': {
                        'chapter_title': 'The Glorious Redeemer, Jerusalem & its Citizens -- Part 2'
                    },
                    '62': {
                        'chapter_title': 'The Glorious Redeemer, Jerusalem & its Citizens -- Part 3'
                    },
                    '63': {
                        'chapter_title': 'Repentance and Confession -- Part 1'
                    },
                    '64': {
                        'chapter_title': 'Repentance and Confession -- Part 2'
                    },
                    '65': {
                        'chapter_title': 'New Heavens and New Earth -- Part 1'
                    },
                    '66': {
                        'chapter_title': 'New Heavens and New Earth -- Part 2'
                    }
                },
                'Jeremiah': {
                    '1': {
                        'chapter_title': 'The Prophet’s Call'
                    },
                    '2': {
                        'chapter_title': 'Israel’s Apostasy'
                    },
                    '3': {
                        'chapter_title': 'Judah Worse Than Israel!'
                    },
                    '4': {
                        'chapter_title': 'Approaching Desolation of Judah'
                    },
                    '5': {
                        'chapter_title': 'Universal Depravity of Judah'
                    },
                    '6': {
                        'chapter_title': 'Destruction From the North (Prophetic)'
                    },
                    '7': {
                        'chapter_title': 'Repentance Their Only Hope'
                    },
                    '8': {
                        'chapter_title': 'The Harvest is Past'
                    },
                    '9': {
                        'chapter_title': 'Jeremiah, the Weeping Prophet'
                    },
                    '10': {
                        'chapter_title': 'Jehovah, the True God'
                    },
                    '11': {
                        'chapter_title': 'The Broken Covenant—Jeremiah’s Death Plotted'
                    },
                    '12': {
                        'chapter_title': 'Jeremiah’s Complaint'
                    },
                    '13': {
                        'chapter_title': 'The Ruined Waistband'
                    },
                    '14': {
                        'chapter_title': 'Drought and Jeremiah’s Intercession -- Part 1'
                    },
                    '15': {
                        'chapter_title': 'Drought and Jeremiah’s Intercession -- Part 2'
                    },
                    '16': {
                        'chapter_title': 'Jeremiah Forbidden to Marry'
                    },
                    '17': {
                        'chapter_title': 'Sabbath Profaned, Judgment Inevitable'
                    },
                    '18': {
                        'chapter_title': 'The Potter’s Clay'
                    },
                    '19': {
                        'chapter_title': 'The Earthen Bottle Broken'
                    },
                    '20': {
                        'chapter_title': 'Jeremiah Imprisoned, Discouraged'
                    },
                    '21': {
                        'chapter_title': 'The Siege Begins'
                    },
                    '22': {
                        'chapter_title': 'Warning to King Jehoiakim'
                    },
                    '23': {
                        'chapter_title': 'False Prophets'
                    },
                    '24': {
                        'chapter_title': 'The Two Baskets of Figs'
                    },
                    '25': {
                        'chapter_title': '70 Years of Captivity Predicted'
                    },
                    '26': {
                        'chapter_title': 'Jeremiah’s Trial Before the Princes'
                    },
                    '27': {
                        'chapter_title': 'Oxen Yoke on Jeremiah’s Neck -- Part 1'
                    },
                    '28': {
                        'chapter_title': 'Oxen Yoke on Jeremiah’s Neck -- Part 2'
                    },
                    '29': {
                        'chapter_title': 'Jeremiah’s Letter to Those in Exile'
                    },
                    '30': {
                        'chapter_title': 'The Great Tribulation'
                    },
                    '31': {
                        'chapter_title': 'The New Covenant'
                    },
                    '32': {
                        'chapter_title': 'Nature of the New Covenant -- Part 1'
                    },
                    '33': {
                        'chapter_title': 'Nature of the New Covenant -- Part 2'
                    },
                    '34': {
                        'chapter_title': 'Zedekiah’s Proclamation of Liberty'
                    },
                    '35': {
                        'chapter_title': 'The Obedience of the Rechabites'
                    },
                    '36': {
                        'chapter_title': 'The King Throws Jeremiah’s Book into the Fire'
                    },
                    '37': {
                        'chapter_title': 'Jeremiah’s Imprisonment -- Part 1'
                    },
                    '38': {
                        'chapter_title': 'Jeremiah’s Imprisonment -- Part 2'
                    },
                    '39': {
                        'chapter_title': 'Jerusalem Burned'
                    },
                    '40': {
                        'chapter_title': 'Gedaliah Made Governor -- Part 1'
                    },
                    '41': {
                        'chapter_title': 'Gedaliah Made Governor -- Part 2'
                    },
                    '42': {
                        'chapter_title': 'Remnant Goes to Egypt -- Part 1'
                    },
                    '43': {
                        'chapter_title': 'Remnant Goes to Egypt -- Part 2'
                    },
                    '44': {
                        'chapter_title': 'Jeremiah’s Final Appeal'
                    },
                    '45': {
                        'chapter_title': 'Baruch (Jeremiah’s Scribe)'
                    },
                    '46': {
                        'chapter_title': 'Prophecy against Egypt'
                    },
                    '47': {
                        'chapter_title': 'Prophecy against the Philistines'
                    },
                    '48': {
                        'chapter_title': 'Prophecy against Moab'
                    },
                    '49': {
                        'chapter_title': 'Prophecy against Ammon, Edom, Syria, Hazor, Elam'
                    },
                    '50': {
                        'chapter_title': 'Prediction of the Fall of Babylon -- Part 1'
                    },
                    '51': {
                        'chapter_title': 'Prediction of the Fall of Babylon -- Part 2'
                    },
                    '52': {
                        'chapter_title': 'Historical Appendix'
                    }
                },
                'Lamentations': {
                    '1': {
                        'chapter_title': 'The Departure of Judah'
                    },
                    '2': {
                        'chapter_title': 'The Devastation of Jehovah'
                    },
                    '3': {
                        'chapter_title': 'The Discernment of Jeremiah'
                    },
                    '4': {
                        'chapter_title': 'The Discipline of Jehovah'
                    },
                    '5': {
                        'chapter_title': 'The Deterrent for Judah'
                    }
                },
                'Ezekiel': {
                    '1': {
                        'chapter_title': 'The Vision of the Glory of God'
                    },
                    '2': {
                        'chapter_title': 'The Voice of God -- Part 1'
                    },
                    '3': {
                        'chapter_title': 'The Voice of God -- Part 2'
                    },
                    '4': {
                        'chapter_title': 'Symbolic Seige of Jerusalem -- Part 1'
                    },
                    '5': {
                        'chapter_title': 'Symbolic Seige of Jerusalem -- Part 2'
                    },
                    '6': {
                        'chapter_title': 'Symbolic Seige of Jerusalem -- Part 3'
                    },
                    '7': {
                        'chapter_title': 'Symbolic Seige of Jerusalem -- Part 4'
                    },
                    '8': {
                        'chapter_title': 'Ezekiel’s Vision—Journey to Jerusalem -- Part 1'
                    },
                    '9': {
                        'chapter_title': 'Ezekiel’s Vision—Journey to Jerusalem -- Part 2'
                    },
                    '10': {
                        'chapter_title': 'Ezekiel’s Vision—Journey to Jerusalem -- Part 3'
                    },
                    '11': {
                        'chapter_title': 'Ezekiel’s Vision—Journey to Jerusalem -- Part 4'
                    },
                    '12': {
                        'chapter_title': 'Ezekiel Moves in his Household Goods'
                    },
                    '13': {
                        'chapter_title': 'False Prophets'
                    },
                    '14': {
                        'chapter_title': 'Hypocritical Inquirers'
                    },
                    '15': {
                        'chapter_title': 'Parable of the Vine Tree'
                    },
                    '16': {
                        'chapter_title': 'Allegory of the Unfaithful Wife'
                    },
                    '17': {
                        'chapter_title': 'Parable of the Two Eagles'
                    },
                    '18': {
                        'chapter_title': '“The Soul That Sins, It Shall Die”'
                    },
                    '19': {
                        'chapter_title': 'The Concluding Lamentation'
                    },
                    '20': {
                        'chapter_title': 'The Filth of Idolatry'
                    },
                    '21': {
                        'chapter_title': 'The Song of the Sword'
                    },
                    '22': {
                        'chapter_title': 'The Sins of Jerusalem'
                    },
                    '23': {
                        'chapter_title': 'Oholah and Oholibah'
                    },
                    '24': {
                        'chapter_title': 'The Boiling Pot'
                    },
                    '25': {
                        'chapter_title': 'Ammon, Moab, Edom, Philistia'
                    },
                    '26': {
                        'chapter_title': 'Tyre and Sidon -- Part 1'
                    },
                    '27': {
                        'chapter_title': 'Tyre and Sidon -- Part 2'
                    },
                    '28': {
                        'chapter_title': 'Tyre and Sidon -- Part 3'
                    },
                    '29': {
                        'chapter_title': 'Egypt (Six Visions) -- Part 1'
                    },
                    '30': {
                        'chapter_title': 'Egypt (Six Visions) -- Part 2'
                    },
                    '31': {
                        'chapter_title': 'Egypt (Six Visions) -- Part 3'
                    },
                    '32': {
                        'chapter_title': 'Egypt (Six Visions) -- Part 4'
                    },
                    '33': {
                        'chapter_title': 'The Watchman'
                    },
                    '34': {
                        'chapter_title': 'The Shepherds'
                    },
                    '35': {
                        'chapter_title': 'Doom of Edom Confirmed'
                    },
                    '36': {
                        'chapter_title': 'New Covenant Confirmed'
                    },
                    '37': {
                        'chapter_title': 'The Valley of Dry Bones'
                    },
                    '38': {
                        'chapter_title': 'Gog and Magog -- Part 1'
                    },
                    '39': {
                        'chapter_title': 'Gog and Magog -- Part 2'
                    },
                    '40': {
                        'chapter_title': 'The Millennial Temple -- Part 1'
                    },
                    '41': {
                        'chapter_title': 'The Millennial Temple -- Part 2'
                    },
                    '42': {
                        'chapter_title': 'The Millennial Temple -- Part 3'
                    },
                    '43': {
                        'chapter_title': 'The Millennial Temple -- Part 4'
                    },
                    '44': {
                        'chapter_title': 'The Millennial Worship -- Part 1'
                    },
                    '45': {
                        'chapter_title': 'The Millennial Worship -- Part 2'
                    },
                    '46': {
                        'chapter_title': 'The Millennial Worship -- Part 3'
                    },
                    '47': {
                        'chapter_title': 'The Millennial Land -- Part 1'
                    },
                    '48': {
                        'chapter_title': 'The Millennial Land -- Part 2'
                    }
                },
                'Daniel': {
                    '1': {
                        'chapter_title': 'The Wisdom of Daniel'
                    },
                    '2': {
                        'chapter_title': 'The Dream Image'
                    },
                    '3': {
                        'chapter_title': 'The Fiery Furnace'
                    },
                    '4': {
                        'chapter_title': 'The Tree Vision of Nebuchadnezzar'
                    },
                    '5': {
                        'chapter_title': 'Belshazzar and the Handwriting on the Wall'
                    },
                    '6': {
                        'chapter_title': 'Daniel in the Lions Den'
                    },
                    '7': {
                        'chapter_title': 'The Four Beasts Vision'
                    },
                    '8': {
                        'chapter_title': 'The Ram and Goat Vision'
                    },
                    '9': {
                        'chapter_title': 'Daniel’s 70 Weeks'
                    },
                    '10': {
                        'chapter_title': 'The Angelic Conflict'
                    },
                    '11': {
                        'chapter_title': 'The Man of Sin'
                    },
                    '12': {
                        'chapter_title': 'The Time of the End'
                    }
                },
                'Hosea': {
                    '1': {
                        'chapter_title': 'Hosea’s Wife and Children -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'Hosea’s Wife and Children -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'Hosea’s Wife and Children -- Part 3'
                    },
                    '4': {
                        'chapter_title': 'Ephraim is Joined to Idols'
                    },
                    '5': {
                        'chapter_title': 'Ephraim Shall Become a Ruin'
                    },
                    '6': {
                        'chapter_title': 'Priests Murder and Commit Lewdness'
                    },
                    '7': {
                        'chapter_title': 'They Are All Adulterers'
                    },
                    '8': {
                        'chapter_title': 'Have Sown the Wind, Shall Reap the Whirlwind'
                    },
                    '9': {
                        'chapter_title': 'Abominable Like the Idols They Love'
                    },
                    '10': {
                        'chapter_title': 'The Glory of Bethel is Departed'
                    },
                    '11': {
                        'chapter_title': 'How Shall I Give You Up?'
                    },
                    '12': {
                        'chapter_title': 'Jacob Found God at Bethel'
                    },
                    '13': {
                        'chapter_title': 'They Sin More and More'
                    },
                    '14': {
                        'chapter_title': 'Israel Shall Return to God'
                    }
                },
                'Joel': {
                    '1': {
                        'chapter_title': 'The Plague of Locusts'
                    },
                    '2': {
                        'chapter_title': 'The Coming Day of the Lord'
                    },
                    '3': {
                        'chapter_title': 'Great Events of the Day of the Lord'
                    }
                },
                'Amos': {
                    '1': {
                        'chapter_title': 'Judgments on Surrounding Nations -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'Judgments on Surrounding Nations -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'The Luxurious Palaces of Samaria'
                    },
                    '4': {
                        'chapter_title': '“Prepare to Meet thy God”'
                    },
                    '5': {
                        'chapter_title': 'The Day of the Lord'
                    },
                    '6': {
                        'chapter_title': 'The Assyrian Captivity'
                    },
                    '7': {
                        'chapter_title': 'Three Visions of Destruction (Locusts, Fire, Plumbline)'
                    },
                    '8': {
                        'chapter_title': 'The Basket of Summer Fruit'
                    },
                    '9': {
                        'chapter_title': 'Future Kingdom Blessing of Restored Israel'
                    }
                },
                'Obadiah': {
                    '1': {
                        'chapter_title': 'The Judgment of Edom - Restoration of Israel'
                    }
                },
                'Jonah': {
                    '1': {
                        'chapter_title': 'Jonah’s Flight'
                    },
                    '2': {
                        'chapter_title': 'Jonah’s Prayer'
                    },
                    '3': {
                        'chapter_title': 'Ninevah’s Repentance'
                    },
                    '4': {
                        'chapter_title': 'Jonah’s Chagrin'
                    }
                },
                'Micah': {
                    '1': {
                        'chapter_title': 'Samaria Doomed'
                    },
                    '2': {
                        'chapter_title': 'Brutality of the Rulers -- Part 1'
                    },
                    '3': {
                        'chapter_title': 'Brutality of the Rulers -- Part 2'
                    },
                    '4': {
                        'chapter_title': 'Prophecy of the Millennial Kingdom'
                    },
                    '5': {
                        'chapter_title': 'Prophecy of Christ’s Birth'
                    },
                    '6': {
                        'chapter_title': 'Jehovah’s Controversy with His People'
                    },
                    '7': {
                        'chapter_title': 'Desolation, But God Will Triump'
                    }
                },
                'Nahum': {
                    '1': {
                        'chapter_title': 'Ninevah Will Be Judged'
                    },
                    '2': {
                        'chapter_title': 'The Judgment is Executed'
                    },
                    '3': {
                        'chapter_title': 'Further Reasons Why'
                    }
                },
                'Habakkuk': {
                    '1': {
                        'chapter_title': 'The Prophet’s Two Dialogues with God -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'The Prophet’s Two Dialogues with God -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'The Prophet’s Prayer and Praise'
                    }
                },
                'Zephaniah': {
                    '1': {
                        'chapter_title': 'The Judgment of God upon Judah'
                    },
                    '2': {
                        'chapter_title': 'The Judgment of God upon Surrounding Nations'
                    },
                    '3': {
                        'chapter_title': 'Millennial Blessings in Israel'
                    }
                },
                'Haggai': {
                    '1': {
                        'chapter_title': 'Two Messages: Rebuke & Commendation'
                    },
                    '2': {
                        'chapter_title': 'Three Messages: Encouragment, Blessing, & Destruction of Gentile Power'
                    }
                },
                'Zechariah': {
                    '1': {
                        'chapter_title': 'Eight Night Visions -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'Eight Night Visions -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'Eight Night Visions -- Part 3'
                    },
                    '4': {
                        'chapter_title': 'Eight Night Visions -- Part 4'
                    },
                    '5': {
                        'chapter_title': 'Eight Night Visions -- Part 5'
                    },
                    '6': {
                        'chapter_title': 'Eight Night Visions & The Crowning of Joshua'
                    },
                    '7': {
                        'chapter_title': 'Question About Fasting -- Part 1'
                    },
                    '8': {
                        'chapter_title': 'Question About Fasting -- Part 2'
                    },
                    '9': {
                        'chapter_title': 'God’s Judgment on Neighbor Nations -- Part 1'
                    },
                    '10': {
                        'chapter_title': 'God’s Judgment on Neighbor Nations -- Part 2'
                    },
                    '11': {
                        'chapter_title': 'God’s Judgment on Neighbor Nations -- Part 3'
                    },
                    '12': {
                        'chapter_title': 'Second Advent and Acceptance of Messiah as King -- Part 1'
                    },
                    '13': {
                        'chapter_title': 'Second Advent and Acceptance of Messiah as King -- Part 2'
                    },
                    '14': {
                        'chapter_title': 'Second Advent and Acceptance of Messiah as King -- Part 3'
                    }
                },
                'Malachi': {
                    '1': {
                        'chapter_title': 'Priests—Get Back into Fellowship'
                    },
                    '2': {
                        'chapter_title': 'Priest’s and People—Get Back into Fellowship'
                    },
                    '3': {
                        'chapter_title': 'Robbery, but Future Blessing'
                    },
                    '4': {
                        'chapter_title': 'The Second Advent'
                    }
                }
            },
            'New Testament': {
                'Matthew': {
                    '1': {
                        'chapter_title': 'The Birth and Reception of the King -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'The Birth and Reception of the King -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'The Baptism of the King'
                    },
                    '4': {
                        'chapter_title': 'The Testing of the King'
                    },
                    '5': {
                        'chapter_title': 'The Proclamation of the King (Sermon on the Mount) -- Part 1'
                    },
                    '6': {
                        'chapter_title': 'The Proclamation of the King (Sermon on the Mount) -- Part 2'
                    },
                    '7': {
                        'chapter_title': 'The Proclamation of the King (Sermon on the Mount) -- Part 3'
                    },
                    '8': {
                        'chapter_title': 'The Authority of the King -- Part 1'
                    },
                    '9': {
                        'chapter_title': 'The Authority of the King -- Part 2'
                    },
                    '10': {
                        'chapter_title': 'The Authority of the King -- Part 3'
                    },
                    '11': {
                        'chapter_title': 'Opposition to the King -- Part 1'
                    },
                    '12': {
                        'chapter_title': 'Opposition to the King -- Part 2'
                    },
                    '13': {
                        'chapter_title': 'The Parables of the King'
                    },
                    '14': {
                        'chapter_title': 'The Revelation and Instruction of the King -- Part 1'
                    },
                    '15': {
                        'chapter_title': 'The Revelation and Instruction of the King -- Part 2'
                    },
                    '16': {
                        'chapter_title': 'The Revelation and Instruction of the King -- Part 3'
                    },
                    '17': {
                        'chapter_title': 'The Revelation and Instruction of the King -- Part 4'
                    },
                    '18': {
                        'chapter_title': 'The Revelation and Instruction of the King -- Part 5'
                    },
                    '19': {
                        'chapter_title': 'The Revelation and Instruction of the King -- Part 6'
                    },
                    '20': {
                        'chapter_title': 'The Revelation and Instruction of the King -- Part 7'
                    },
                    '21': {
                        'chapter_title': 'The Formal Presentation of the King (Palm Sunday) -- Part 1'
                    },
                    '22': {
                        'chapter_title': 'The Formal Presentation of the King (Palm Sunday) -- Part 2'
                    },
                    '23': {
                        'chapter_title': 'The Formal Presentation of the King (Palm Sunday) -- Part 3'
                    },
                    '24': {
                        'chapter_title': 'The Predictions of the King (Mt. Olivet Discourse) -- Part 1'
                    },
                    '25': {
                        'chapter_title': 'The Predictions of the King (Mt. Olivet Discourse) -- Part 2'
                    },
                    '26': {
                        'chapter_title': 'The Crucifixion of the King -- Part 1'
                    },
                    '27': {
                        'chapter_title': 'The Crucifixion of the King -- Part 2'
                    },
                    '28': {
                        'chapter_title': 'The Resurrection of the King'
                    }
                },
                'Mark': {
                    '1': {
                        'chapter_title': 'Preparation of the Servant'
                    },
                    '2': {
                        'chapter_title': 'Galilean Ministry of the Servant -- Part 1'
                    },
                    '3': {
                        'chapter_title': 'Galilean Ministry of the Servant -- Part 2'
                    },
                    '4': {
                        'chapter_title': 'Galilean Ministry of the Servant -- Part 3'
                    },
                    '5': {
                        'chapter_title': 'Galilean Ministry of the Servant -- Part 4'
                    },
                    '6': {
                        'chapter_title': 'Galilean Ministry of the Servant -- Part 5'
                    },
                    '7': {
                        'chapter_title': 'Galilean Ministry of the Servant -- Part 6'
                    },
                    '8': {
                        'chapter_title': 'NE of Galilee Ministry of the Servant -- Part 1'
                    },
                    '9': {
                        'chapter_title': 'NE of Galilee Ministry of the Servant -- Part 2'
                    },
                    '10': {
                        'chapter_title': 'Enroute to Jerusalem Ministry of the Servant'
                    },
                    '11': {
                        'chapter_title': 'Jerusalem Ministry of the Servant -- Part 1'
                    },
                    '12': {
                        'chapter_title': 'Jerusalem Ministry of the Servant -- Part 2'
                    },
                    '13': {
                        'chapter_title': 'Jerusalem Ministry of the Servant -- Part 3'
                    },
                    '14': {
                        'chapter_title': 'Crucifixion of the Servant -- Part 1'
                    },
                    '15': {
                        'chapter_title': 'Crucifixion of the Servant -- Part 2'
                    },
                    '16': {
                        'chapter_title': 'Resurrection of the Servant'
                    }
                },
                'Luke': {
                    '1': {
                        'chapter_title': 'The Identification of the Son of Man with Men -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'The Identification of the Son of Man with Men -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'The Identification of the Son of Man with Men -- Part 3'
                    },
                    '4': {
                        'chapter_title': 'The Identification of the Son of Man with Men -- Part 4'
                    },
                    '5': {
                        'chapter_title': 'The Ministry of the Son of Man to Men -- Part 1'
                    },
                    '6': {
                        'chapter_title': 'The Ministry of the Son of Man to Men -- Part 2'
                    },
                    '7': {
                        'chapter_title': 'The Ministry of the Son of Man to Men -- Part 3'
                    },
                    '8': {
                        'chapter_title': 'The Ministry of the Son of Man to Men -- Part 4'
                    },
                    '9': {
                        'chapter_title': 'The Ministry of the Son of Man to Men -- Part 5'
                    },
                    '10': {
                        'chapter_title': 'The Ministry of the Son of Man to Men -- Part 6'
                    },
                    '11': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 2'
                    },
                    '12': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 3'
                    },
                    '13': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 4'
                    },
                    '14': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 5'
                    },
                    '15': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 6'
                    },
                    '16': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 7'
                    },
                    '17': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 8'
                    },
                    '18': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 9'
                    },
                    '19': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 10'
                    },
                    '20': {
                        'chapter_title': 'The Rejection of the Son of Man by Men -- Part 11'
                    },
                    '21': {
                        'chapter_title': 'The Suffering of the Son of Man for Men -- Part 1'
                    },
                    '22': {
                        'chapter_title': 'The Suffering of the Son of Man for Men -- Part 2'
                    },
                    '23': {
                        'chapter_title': 'The Suffering of the Son of Man for Men -- Part 3'
                    },
                    '24': {
                        'chapter_title': 'The Resurrection of the Son of Man before Men'
                    }
                },
                'John': {
                    '1': {
                        'chapter_title': 'Christ the Word'
                    },
                    '2': {
                        'chapter_title': 'Christ the Creator'
                    },
                    '3': {
                        'chapter_title': 'Christ the Saviour'
                    },
                    '4': {
                        'chapter_title': 'Christ the Water of Life'
                    },
                    '5': {
                        'chapter_title': 'Christ the Judge'
                    },
                    '6': {
                        'chapter_title': 'Christ the Bread of Life'
                    },
                    '7': {
                        'chapter_title': 'Christ the Heavenly One'
                    },
                    '8': {
                        'chapter_title': 'Christ the Light of the World -- Part 1'
                    },
                    '9': {
                        'chapter_title': 'Christ the Light of the World -- Part 2'
                    },
                    '10': {
                        'chapter_title': 'Christ the Good Shepherd'
                    },
                    '11': {
                        'chapter_title': 'Christ the Resurrection and the Life'
                    },
                    '12': {
                        'chapter_title': 'Christ the Center of Attraction'
                    },
                    '13': {
                        'chapter_title': 'Christ the Advocate'
                    },
                    '14': {
                        'chapter_title': 'Christ the Coming One'
                    },
                    '15': {
                        'chapter_title': 'Christ the Vine'
                    },
                    '16': {
                        'chapter_title': 'Christ the Pre-Eminent One'
                    },
                    '17': {
                        'chapter_title': 'Christ the Intercessor (High Priest)'
                    },
                    '18': {
                        'chapter_title': 'Christ the Faithful and Obedient One unto Death -- Part 1'
                    },
                    '19': {
                        'chapter_title': 'Christ the Faithful and Obedient One unto Death -- Part 2'
                    },
                    '20': {
                        'chapter_title': 'Christ the Victorious One'
                    },
                    '21': {
                        'chapter_title': 'Christ the Great Shepherd'
                    }
                },
                'Acts': {
                    '1': {
                        'chapter_title': 'Commission and Ascension'
                    },
                    '2': {
                        'chapter_title': 'Pentecost'
                    },
                    '3': {
                        'chapter_title': 'Lame Man Healed'
                    },
                    '4': {
                        'chapter_title': 'The First Persecution'
                    },
                    '5': {
                        'chapter_title': 'Ananias and Sapphira'
                    },
                    '6': {
                        'chapter_title': 'The First Deacons'
                    },
                    '7': {
                        'chapter_title': 'Stephen and Martyrdom'
                    },
                    '8': {
                        'chapter_title': 'Philip and the Eunuch'
                    },
                    '9': {
                        'chapter_title': 'Saul’s Conversion on the Damascus Road'
                    },
                    '10': {
                        'chapter_title': 'Peter and Cornelius'
                    },
                    '11': {
                        'chapter_title': 'Peter Vindicates Ministry to the Gentiles'
                    },
                    '12': {
                        'chapter_title': 'Peter in Prison'
                    },
                    '13': {
                        'chapter_title': '1st Missionary Journey -- Part 1'
                    },
                    '14': {
                        'chapter_title': '1st Missionary Journey -- Part 2'
                    },
                    '15': {
                        'chapter_title': 'Jerusalem Council'
                    },
                    '16': {
                        'chapter_title': '2nd Missionary Journey -- Part 1'
                    },
                    '17': {
                        'chapter_title': '2nd Missionary Journey -- Part 2'
                    },
                    '18': {
                        'chapter_title': '2nd Missionary Journey -- Part 3'
                    },
                    '19': {
                        'chapter_title': '3rd Missionary Journey -- Part 1'
                    },
                    '20': {
                        'chapter_title': '3rd Missionary Journey -- Part 2'
                    },
                    '21': {
                        'chapter_title': 'Paul Arrives at Jerusalem'
                    },
                    '22': {
                        'chapter_title': 'Paul’s Defense Before the Multitudes'
                    },
                    '23': {
                        'chapter_title': 'Defense Before Sanhedrin'
                    },
                    '24': {
                        'chapter_title': 'Before Felix'
                    },
                    '25': {
                        'chapter_title': 'Before Festus'
                    },
                    '26': {
                        'chapter_title': 'Before King Agrippa'
                    },
                    '27': {
                        'chapter_title': 'Shipwreck'
                    },
                    '28': {
                        'chapter_title': 'Rome'
                    }
                },
                'Romans': {
                    '1': {
                        'chapter_title': 'All Gentiles Under Sin'
                    },
                    '2': {
                        'chapter_title': 'All Jews Under Sin'
                    },
                    '3': {
                        'chapter_title': 'All Have Sinned'
                    },
                    '4': {
                        'chapter_title': 'Justification by Faith -- Part 1'
                    },
                    '5': {
                        'chapter_title': 'Justification by Faith -- Part 2'
                    },
                    '6': {
                        'chapter_title': 'The Christian Walk -- Part 1'
                    },
                    '7': {
                        'chapter_title': 'The Christian Walk -- Part 2'
                    },
                    '8': {
                        'chapter_title': 'The Christian Walk -- Part 3'
                    },
                    '9': {
                        'chapter_title': 'Israel in Prophecy'
                    },
                    '10': {
                        'chapter_title': 'Israel in Failure'
                    },
                    '11': {
                        'chapter_title': 'Israel in Success'
                    },
                    '12': {
                        'chapter_title': 'Living Sacrifice'
                    },
                    '13': {
                        'chapter_title': 'Love Your Neighbor'
                    },
                    '14': {
                        'chapter_title': 'Discerning the Doubtful'
                    },
                    '15': {
                        'chapter_title': 'Jew & Gentile, One in Christ'
                    },
                    '16': {
                        'chapter_title': 'Paul’s Friends'
                    }
                },
                '1st Corinthians': {
                    '1': {
                        'chapter_title': 'Divisions'
                    },
                    '2': {
                        'chapter_title': 'Natural, Carnal, Spiritual Man'
                    },
                    '3': {
                        'chapter_title': 'Judgment Seat of Christ'
                    },
                    '4': {
                        'chapter_title': 'Judging Each Other'
                    },
                    '5': {
                        'chapter_title': 'Immorality Rebuked'
                    },
                    '6': {
                        'chapter_title': 'Lawsuits With Christians'
                    },
                    '7': {
                        'chapter_title': 'Christian Marriage'
                    },
                    '8': {
                        'chapter_title': 'Meats Offered to Idols'
                    },
                    '9': {
                        'chapter_title': 'Castaway Chapter'
                    },
                    '10': {
                        'chapter_title': 'Israel’s Bad Example'
                    },
                    '11': {
                        'chapter_title': 'Conduct at the Lord’s Supper'
                    },
                    '12': {
                        'chapter_title': 'Spiritual Gifts'
                    },
                    '13': {
                        'chapter_title': 'Love Chapter'
                    },
                    '14': {
                        'chapter_title': 'Spiritual Gifts'
                    },
                    '15': {
                        'chapter_title': 'Resurrection Chapter'
                    },
                    '16': {
                        'chapter_title': 'Closing Instructions'
                    }
                },
                '2nd Corinthians': {
                    '1': {
                        'chapter_title': 'Paul’s Plan to Come to Corinth'
                    },
                    '2': {
                        'chapter_title': 'Immoral Man Cleansed'
                    },
                    '3': {
                        'chapter_title': 'The Glorious Ministry'
                    },
                    '4': {
                        'chapter_title': 'The Suffering Ministry'
                    },
                    '5': {
                        'chapter_title': 'The Reconciling Ministry'
                    },
                    '6': {
                        'chapter_title': 'The Separated Ministry'
                    },
                    '7': {
                        'chapter_title': 'The Heart of Paul'
                    },
                    '8': {
                        'chapter_title': 'Money Matters'
                    },
                    '9': {
                        'chapter_title': 'Cheerful Giving'
                    },
                    '10': {
                        'chapter_title': 'Divine Viewpoint vs. Human Viewpoint'
                    },
                    '11': {
                        'chapter_title': 'The Boasting of Paul'
                    },
                    '12': {
                        'chapter_title': 'The Third Heaven and the Thorn'
                    },
                    '13': {
                        'chapter_title': 'Concluding Remarks'
                    }
                },
                'Galatians': {
                    '1': {
                        'chapter_title': 'Gospel Perversion by False Teachers'
                    },
                    '2': {
                        'chapter_title': 'Legalism vs. Grace'
                    },
                    '3': {
                        'chapter_title': 'Abrahamic Covenant'
                    },
                    '4': {
                        'chapter_title': 'The Curse of Legalism'
                    },
                    '5': {
                        'chapter_title': 'Walk in the Spirit, Fruit of the Spirit (inward)'
                    },
                    '6': {
                        'chapter_title': 'Walk in the Spirit, Ministry to Others (outward)'
                    }
                },
                'Ephesians': {
                    '1': {
                        'chapter_title': 'The Doctrinal Wealth of the Christian -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'The Doctrinal Wealth of the Christian -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'The Walk of the Christian -- Part 1'
                    },
                    '4': {
                        'chapter_title': 'The Walk of the Christian -- Part 2'
                    },
                    '5': {
                        'chapter_title': 'The Warfare of the Christian -- Part 1'
                    },
                    '6': {
                        'chapter_title': 'The Warfare of the Christian -- Part 2'
                    }
                },
                'Philippians': {
                    '1': {
                        'chapter_title': 'The Mind of Paul'
                    },
                    '2': {
                        'chapter_title': 'The Mind of Christ'
                    },
                    '3': {
                        'chapter_title': 'That I May Know Him'
                    },
                    '4': {
                        'chapter_title': 'What Believers Should Think'
                    }
                },
                'Colossians': {
                    '1': {
                        'chapter_title': '7 Superiorities of Christ'
                    },
                    '2': {
                        'chapter_title': 'God is Complete'
                    },
                    '3': {
                        'chapter_title': 'Fruit of Union With Christ'
                    },
                    '4': {
                        'chapter_title': 'Godly Examples—Tychicus, Onesimus, Epaphras'
                    }
                },
                '1st Thessalonians': {
                    '1': {
                        'chapter_title': 'Work of Faith, Labor of Love, Steadfastness of Hope'
                    },
                    '2': {
                        'chapter_title': 'Testimony of Paul'
                    },
                    '3': {
                        'chapter_title': 'Timothy’s Report to Paul'
                    },
                    '4': {
                        'chapter_title': 'Rapture Chapter'
                    },
                    '5': {
                        'chapter_title': 'Peace and Safety—Then Sudden Destruction'
                    }
                },
                '2nd Thessalonians': {
                    '1': {
                        'chapter_title': 'Comfort in Persecution'
                    },
                    '2': {
                        'chapter_title': 'The Man of Sin Revealed'
                    },
                    '3': {
                        'chapter_title': 'Disorderly Christians and Busybodies'
                    }
                },
                '1st Timothy': {
                    '1': {
                        'chapter_title': 'Legalism & Unsound Teaching Rebuked'
                    },
                    '2': {
                        'chapter_title': 'Prayer for Government Leaders'
                    },
                    '3': {
                        'chapter_title': 'Qualifications for Pastors & Deacons'
                    },
                    '4': {
                        'chapter_title': 'Doctrine of Demons vs. Good Doctrine'
                    },
                    '5': {
                        'chapter_title': 'The Ministry of Widows'
                    },
                    '6': {
                        'chapter_title': 'The Christian in Business'
                    }
                },
                '2nd Timothy': {
                    '1': {
                        'chapter_title': 'Lois, Eunice, Timothy'
                    },
                    '2': {
                        'chapter_title': 'A Good Soldier Studies'
                    },
                    '3': {
                        'chapter_title': 'Verbal Inspiration Chapter'
                    },
                    '4': {
                        'chapter_title': 'Paul’s Thinking Two Months Before Death'
                    }
                },
                'Titus': {
                    '1': {
                        'chapter_title': 'Crete & Christianity'
                    },
                    '2': {
                        'chapter_title': 'Looking for that Blessed Hope'
                    },
                    '3': {
                        'chapter_title': 'Production of Divine Good'
                    },
                    '4': {
                        'chapter_title': 'Rejection of Heretics'
                    }
                },
                'Philemon': {
                    '1': {
                        'chapter_title': 'Effectual, Profitable Christianity'
                    }
                },
                'Hebrews': {
                    '1': {
                        'chapter_title': 'Angelic Conflict: Christ is Better than the Angels'
                    },
                    '2': {
                        'chapter_title': 'Angelic Conflict: Christ Made Lower than the Angels'
                    },
                    '3': {
                        'chapter_title': 'Christ is Better than Moses'
                    },
                    '4': {
                        'chapter_title': 'The Faith-Rest Technique'
                    },
                    '5': {
                        'chapter_title': 'Christ Our High Priest'
                    },
                    '6': {
                        'chapter_title': 'On to Maturity'
                    },
                    '7': {
                        'chapter_title': 'Melchizedek vs. Aaronic Priesthood'
                    },
                    '8': {
                        'chapter_title': 'New Covenant vs. Mosaic Covenant'
                    },
                    '9': {
                        'chapter_title': 'The Blood of Christ'
                    },
                    '10': {
                        'chapter_title': 'In the Holiest'
                    },
                    '11': {
                        'chapter_title': 'The Hall of Faith'
                    },
                    '12': {
                        'chapter_title': 'Chastisement Chapter'
                    },
                    '13': {
                        'chapter_title': 'Bearing His Reproach'
                    }
                },
                'James': {
                    '1': {
                        'chapter_title': 'Ask For Wisdom Chapter'
                    },
                    '2': {
                        'chapter_title': 'Relationship of Faith and Works'
                    },
                    '3': {
                        'chapter_title': 'Tongue Chapter'
                    },
                    '4': {
                        'chapter_title': 'The Rebuke of Worldliness'
                    },
                    '5': {
                        'chapter_title': 'Practical Pointers on Riches, Patience, & Prayer'
                    }
                },
                '1st Peter': {
                    '1': {
                        'chapter_title': 'The Trial of Your Faith is Precious'
                    },
                    '2': {
                        'chapter_title': 'Suffering in the Light of His Suffering'
                    },
                    '3': {
                        'chapter_title': 'How to Win a Negative Husband'
                    },
                    '4': {
                        'chapter_title': 'Strange Trials and Suffering'
                    },
                    '5': {
                        'chapter_title': 'Christian Service—Leaders and People'
                    }
                },
                '2nd Peter': {
                    '1': {
                        'chapter_title': 'The Great and Precious Promises'
                    },
                    '2': {
                        'chapter_title': 'False Teachers'
                    },
                    '3': {
                        'chapter_title': 'Burning of the Present Heavens and Earth'
                    }
                },
                '1st John': {
                    '1': {
                        'chapter_title': 'Christ is Light -- Part 1'
                    },
                    '2': {
                        'chapter_title': 'Christ is Light -- Part 2'
                    },
                    '3': {
                        'chapter_title': 'Christ is Love -- Part 1'
                    },
                    '4': {
                        'chapter_title': 'Christ is Love -- Part 2'
                    },
                    '5': {
                        'chapter_title': 'Christ is Life'
                    }
                },
                '2nd John': {
                    '1': {
                        'chapter_title': 'Truth vs. Error'
                    }
                },
                '3rd John': {
                    '1': {
                        'chapter_title': 'Hospitality'
                    }
                },
                'Jude': {
                    '1': {
                        'chapter_title': 'Contending for the Faith'
                    }
                },
                'Revelation': {
                    '1': {
                        'chapter_title': 'Introduction'
                    },
                    '2': {
                        'chapter_title': 'The Seven Churches -- Part 1'
                    },
                    '3': {
                        'chapter_title': 'The Seven Churches -- Part 2'
                    },
                    '4': {
                        'chapter_title': 'The Heavens Opened'
                    },
                    '5': {
                        'chapter_title': 'The Seven Seals'
                    },
                    '6': {
                        'chapter_title': 'The Seven Seals Opened'
                    },
                    '7': {
                        'chapter_title': 'Sealing of the 144,000'
                    },
                    '8': {
                        'chapter_title': 'The Seven Trumpets'
                    },
                    '9': {
                        'chapter_title': 'The Trumpets Opened'
                    },
                    '10': {
                        'chapter_title': 'The Mighty Angel and the Little Book'
                    },
                    '11': {
                        'chapter_title': 'The Two Witnesses'
                    },
                    '12': {
                        'chapter_title': 'The Seven Personages'
                    },
                    '13': {
                        'chapter_title': 'The Sea Beast and the Earth Beast'
                    },
                    '14': {
                        'chapter_title': 'Vision of the Lamb & the 144,000'
                    },
                    '15': {
                        'chapter_title': 'The Seven Vials'
                    },
                    '16': {
                        'chapter_title': 'The Vials Opened'
                    },
                    '17': {
                        'chapter_title': 'Religious Babylon'
                    },
                    '18': {
                        'chapter_title': 'Commercial Babylon'
                    },
                    '19': {
                        'chapter_title': 'The Second Advent'
                    },
                    '20': {
                        'chapter_title': 'The Great White Throne'
                    },
                    '21': {
                        'chapter_title': 'The New Heavens, New Earth, & New Jerusalem'
                    },
                    '22': {
                        'chapter_title': 'Eternity'
                    }
                }
            }
        }

    def MakeBible(self):
        self.fetch_bible()
        self.add_bible_text()
        self.save_bible()

    def download_needed(self, filename):
        retval = True
        print(filename.name)
        if filename.exists():
            stat = filename.stat()
            now = time.time()
            hours_old = int((now - stat.st_mtime) / 3600)
            if hours_old < self.max_file_age_hours:
                retval = False
        return retval

    def fetch_bible(self):
        if self.download_needed(self.bpath.bible_save):
            response = self.get_url(self.bpath.bible_url, zip=True)
            if response.status_code == self.data_OK:
                with self.bpath.bible_save.open('wb') as f:
                    f.write(response.content)
                with zipfile.ZipFile(self.bpath.bible_save, 'r') as zip_ref:
                    zip_ref.extractall(self.bpath.KingJamespath)
            else:
                self.em.error_msg(message='Network error', title='King James Bible download')




    def save_bible(self):
        with self.bpath.IndexedBible.open('w') as f:
            json.dump(self.Bible, f)

    def get_id(self, word):
        pos = word.index(':')
        chapter = word[1:pos]
        verse = word[pos+1:-1]
        return chapter, verse

    def first_pass(self, filename):
        newfilename = self.bpath.tmpdir / f'{filename.stem}_tmp{filename.suffix}'
        firstline = True
        buffer = ''
        with filename.open() as f, newfilename.open('w') as fo:
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue
                line_list = line.split()
                for n, word in enumerate(line_list):
                    if word.startswith('{'):
                        if firstline:
                            chapter, verse = self.get_id(word)
                            firstline = False
                        else:
                            buffer = buffer.strip()
                            buffer = f'\n{buffer}'
                        fo.write(buffer)
                        chapter, verse = self.get_id(word)
                        buffer = f'{chapter}|{verse}|'
                        continue
                    else:
                        buffer = f'{buffer} {word}'
            if len(buffer) > 0:
                buffer = buffer.strip()
                buffer = f'\n{buffer}\n'
                fo.write(buffer)
        return newfilename

    def book_parse(self, volume, book, filename):
        filename = self.first_pass(filename)
        with filename.open() as f:
            for line in f:
                line = line.strip()
                line = line.split('|')
                if len(line) == 1:
                    self.Bible[volume][book]['chapter_title'] = line
                else:
                    chapter = line[0]
                    verse = line[1]
                    text = line[2].strip()
                    try:
                        self.Bible[volume][book][chapter][verse] = text
                    except KeyError:
                        print(f'Error: Volume: {volume}, book: {book}, chapter: {chapter}, verse: {verse}')


    def add_bible_text(self):
        for volume, contents in self.Bible.items():
            for book, detail in contents.items():
                filename = self.bpath.KingJamespath / self.book_xref[book]
                # filename = self.bpath.KingJamespath / f'{book}.txt'
                self.book_parse(volume, book, filename)

if __name__ == '__main__':
   ccj =  CreateChapterJson()
   ccj.MakeBible()
