import random
import copy

Course_Morning = {
        'ARTIFICIAL INTELLIGENCE': ['E1+TE1'],
        'OPERATING SYSTEMS': ['B1+TB1'],
        'OPERATING SYSTEMS LAB': [
            'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 'L39+L40',
            'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50',
            'L51+L52', 'L53+L54', 'L55+L56', 'L57+L58', 'L59+L60'
        ],
        'AWS SOLUTIONS ARCHITECT': ['F1+TF1'],
        'COMPILER DESIGN': ['C1+TC1'],
        'COMPILER DESIGN LAB':[
            'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 'L39+L40',
            'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50',
            'L51+L52', 'L53+L54', 'L55+L56', 'L57+L58', 'L59+L60'
        ],
        'DATABASE SYSTEMS': ['A1+TA1'],
        'DATABASE SYSTEMS LAB': [
            'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 'L39+L40',
            'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50',
            'L51+L52', 'L53+L54', 'L55+L56', 'L57+L58', 'L59+L60'
        ],
        'COMPUTER NETWORKS': ['D1+TD1'],
        'COMPUTER NETWORKS LAB': [
            'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 'L39+L40',
            'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50',
            'L51+L52', 'L53+L54', 'L55+L56', 'L57+L58', 'L59+L60'
        ],
        'ADVANCED COMPETITIVE CODING': ['G1+TG1'],
}
Course_Evening ={
        'ARTIFICIAL INTELLIGENCE': ['E2+TE2'],
        'OPERATING SYSTEMS': ['B2+TB2'],
        'OPERATING SYSTEMS LAB': [
            'L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10',
            'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20',
            'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30'
        ],
        'AWS SOLUTIONS ARCHITECT': ['F2+TF2'],
        'COMPILER DESIGN': ['C2+TC2'],
        'COMPILER DESIGN LAB': [
            'L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10',
            'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20',
            'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30'
        ],
        'DATABASE SYSTEMS': ['A2+TA2'],
        'DATABASE SYSTEMS LAB': [
            'L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10',
            'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20',
            'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30'
        ],
        'COMPUTER NETWORKS': ['D2+TD2'],
        'COMPUTER NETWORKS LAB': [
            'L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10',
            'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20',
            'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30'
        ],
        'ADVANCED COMPETITIVE CODING': ['G2+TG2']
    }


# Example usage in the main timetable generation
## For the morning timetable
courses_details_morning = {
    "Artificial Intelligence": [
        {"Slot": "E1+TE1", "Location": "SJT501", "Faculty": "JAISHANKAR N"},
        {"Slot": "E1+TE1", "Location": "SJT502", "Faculty": "SARVANAGURU RA.K"},
        {"Slot": "E1+TE1", "Location": "SJT508", "Faculty": "AKILA VECTOR"},
        {"Slot": "E1+TE1", "Location": "SJT505", "Faculty": "NAGA RAJA G"},
        {"Slot": "E1+TE1", "Location": "SJT513", "Faculty": "ILANTHERAL K P S K"},
        {"Slot": "E1+TE1", "Location": "SJT603", "Faculty": "RISHIN HALDAR"},
        {"Slot": "E1+TE1", "Location": "SJT503", "Faculty": "RAJAKUMAR K"},
        {"Slot": "E1+TE1", "Location": "SJT504", "Faculty": "VISHWANATHAN P"},
        {"Slot": "E1+TE1", "Location": "SJT522", "Faculty": "BALAMURGAN R"},
        {"Slot": "E1+TE1", "Location": "SJT702", "Faculty": "SRIDHAR RAJ S"},
        {"Slot": "E1+TE1", "Location": "SJT604", "Faculty": "JAYASHREE J"},
        {"Slot": "E1+TE1", "Location": "SJT521", "Faculty": "NAVAMANI T M"},
        {"Slot": "E1+TE1", "Location": "SJT601", "Faculty": "SUDARSHAN NANDY"},
        {"Slot": "E1+TE1", "Location": "SJT707", "Faculty": "NAGA PRIYADARSHINI R"},
        {"Slot": "E1+TE1", "Location": "SJT709", "Faculty": "MOHAN KUMAR P"},
        {"Slot": "E1+TE1", "Location": "SJT626", "Faculty": "JAGALINGAM P"},
        {"Slot": "E1+TE1", "Location": "SJT602 A", "Faculty": "SHALINI L"},
        {"Slot": "E1+TE1", "Location": "SJT627", "Faculty": "MOHANA CM"},
        {"Slot": "E1+TE1", "Location": "SJT703", "Faculty": "SUNIJA A P"},
        {"Slot": "E1+TE1", "Location": "SJT704", "Faculty": "SAMRIDDHI SARKAR"},
        {"Slot": "E1+TE1", "Location": "SJT710", "Faculty": "RAJAY VEDARAJ I.S"}
    ],
    "Operating Systems": [
        {"Slot": "B1+TB1", "Location": "SJT508", "Faculty": "PERPI RAJARAJESWARI"},
        {"Slot": "B1+TB1", "Location": "SJT513", "Faculty": "NAVEENKUMAR J"},
        {"Slot": "B1+TB1", "Location": "SJT522", "Faculty": "BHULAKSHMI BONTHU"},
        {"Slot": "B1+TB1", "Location": "SJT627", "Faculty": "SIVAPRAKASH S"},
        {"Slot": "B1+TB1", "Location": "SJT702", "Faculty": "KUMARESAN A"},
        {"Slot": "B1+TB1", "Location": "SJT501", "Faculty": "ANISHA M.LAL"},
        {"Slot": "B1+TB1", "Location": "SJT503", "Faculty": "SENDHIL KUMAR K.S"},
        {"Slot": "B1+TB1", "Location": "SJT502", "Faculty": "SIVAKUMAR N"},
        {"Slot": "B1+TB1", "Location": "SJT504", "Faculty": "NARAYAN PRASANTH"},
        {"Slot": "B1+TB1", "Location": "SJT505", "Faculty": "ANTO S"},
        {"Slot": "B1+TB1", "Location": "SJT521", "Faculty": "SURESH P"},
        {"Slot": "B1+TB1", "Location": "SJT602A", "Faculty": "DEEPA .K"},
        {"Slot": "B1+TB1", "Location": "SJT601", "Faculty": "USHUS ELIZEBETH ZACHARIAH"},
        {"Slot": "B1+TB1", "Location": "SJT603", "Faculty": "RUBY D"},
        {"Slot": "B1+TB1", "Location": "SJT604", "Faculty": "HITESHWAR KUMAR AZAD"},
        {"Slot": "B1+TB1", "Location": "SJT626", "Faculty": "NIHA K"},
        {"Slot": "B1+TB1", "Location": "SJT704", "Faculty": "BALAJI N"},
        {"Slot": "B1+TB1", "Location": "SJT709", "Faculty": "MOHANKUMAR B"},
        {"Slot": "B1+TB1", "Location": "SJT707", "Faculty": "YOGANAND S"},
        {"Slot": "B1+TB1", "Location": "SJT710", "Faculty": "EZHIL ARASI V"},
        {"Slot": "B1+TB1", "Location": "SJT712", "Faculty": "PADMAVATHY T"},
        {"Slot": "B1+TB1", "Location": "SJT703", "Faculty": "MALINI S"},
        {"Slot": "B1+TB1", "Location": "SJT711", "Faculty": "RAHUL SRIVASTAVA"}
    ],
    "Aws Solutions Architect": [
        {"Slot": "F1+TF1", "Location": "SJT601", "Faculty": "BALKRISHNAN P"},
        {"Slot": "F1+TF1", "Location": "SJT602A", "Faculty": "JOTHI K R"},
        {"Slot": "F1+TF1", "Location": "SJT604", "Faculty": "JUSTIN GOPINATH A"},
        {"Slot": "F1+TF1", "Location": "SJT626", "Faculty": "KANAGARAJ R"},
        {"Slot": "F1+TF1", "Location": "SJT627", "Faculty": "KARTHIK G M"},
        {"Slot": "F1+TF1", "Location": "SJT702", "Faculty": "KOPPERUNDEVI N"},
        {"Slot": "F1+TF1", "Location": "SJT703", "Faculty": "PARTHASARTHY G"},
        {"Slot": "F1+TF1", "Location": "SJT704", "Faculty": "THURAI RANDIAN M"},
        {"Slot": "F1+TF1", "Location": "SJT707", "Faculty": "UMAMAHESWARI M"},
        {"Slot": "F1+TF1", "Location": "SJT710", "Faculty": "GOUTAM MAJUMDER"},
        {"Slot": "F1+TF1", "Location": "SJT709", "Faculty": "KONATHAM SUMALATHA"},
        {"Slot": "F1+TF1", "Location": "SJT501", "Faculty": "NARAYANAMOORTHI M"},
        {"Slot": "F1+TF1", "Location": "SJT502", "Faculty": "GOVINDA K"},
        {"Slot": "F1+TF1", "Location": "SJT503", "Faculty": "MYTHILI T"},
        {"Slot": "F1+TF1", "Location": "SJT508", "Faculty": "SRIVANI A"},
        {"Slot": "F1+TF1", "Location": "SJT505", "Faculty": "ARCHANA T"},
        {"Slot": "F1+TF1", "Location": "SJT504", "Faculty": "ABDUL GAFFAR H"},
        {"Slot": "F1+TF1", "Location": "SJT715", "Faculty": "SANJIBAN SEKHAR ROY"},
        {"Slot": "F1+TF1", "Location": "SJT513", "Faculty": "SUDHA.S"},
        {"Slot": "F1+TF1", "Location": "SJT521", "Faculty": "NARESH K"},
        {"Slot": "F1+TF1", "Location": "SJT522", "Faculty": "GOPICHAND G"},
        {"Slot": "F1+TF1", "Location": "SJT603", "Faculty": "VINILA JINNY"},
        {"Slot": "F1+TF1", "Location": "SJT712", "Faculty": "PRIYA G"},
        {"Slot": "F1+TF1", "Location": "SJT711", "Faculty": "JAYAKUMAR S"}
    ],
    "Compiler Design": [
        {"Slot": "C1+TC1", "Location": "SJT521", "Faculty": "SATHYA K"},
        {"Slot": "C1+TC1", "Location": "SJT703", "Faculty": "BHAVANA TYAGI"},
        {"Slot": "C1+TC1", "Location": "SJT704", "Faculty": "DEBI PRASANNA ACHARJYA"},
        {"Slot": "C1+TC1", "Location": "SJT501", "Faculty": "SAHAAYA ARUL MARY S A"},
        {"Slot": "C1+TC1", "Location": "SJT502", "Faculty": "KANNADASAN R"},
        {"Slot": "C1+TC1", "Location": "SJT513", "Faculty": "KALAIVANI K"},
        {"Slot": "C1+TC1", "Location": "SJT503", "Faculty": "VISHNUPRIYA"},
        {"Slot": "C1+TC1", "Location": "SJT504", "Faculty": "BHUVANESWARI M"},
        {"Slot": "C1+TC1", "Location": "SJT505", "Faculty": "VETRISELVI T"},
        {"Slot": "C1+TC1", "Location": "SJT508", "Faculty": "KANAGARAJ R"},
        {"Slot": "C1+TC1", "Location": "SJT601", "Faculty": "SABYASACHI KAMILA"},
        {"Slot": "C1+TC1", "Location": "SJT626", "Faculty": "ISLABUDEEN M"},
        {"Slot": "C1+TC1", "Location": "SJT627", "Faculty": "SUGANTHINI C"},
        {"Slot": "C1+TC1", "Location": "SJT522", "Faculty": "BASKARAN P"},
        {"Slot": "C1+TC1", "Location": "SJT602A", "Faculty": "UMA PRIYA D"},
        {"Slot": "C1+TC1", "Location": "SJT707", "Faculty": "BAIJU B V"},
        {"Slot": "C1+TC1", "Location": "SJT315", "Faculty": "NAVEEN MISHRA"},
        {"Slot": "C1+TC1", "Location": "SJT603", "Faculty": "MUKKU NISANTH KARTHEEK"},
        {"Slot": "C1+TC1", "Location": "SJT604", "Faculty": "ARUMUGA ARUN R"},
        {"Slot": "C1+TC1", "Location": "SJT702", "Faculty": "NAGA PRIYADARSHINI R"}
    ],
    "Compiler Design Lab": [
        {"Slot": "L31+L32", "Location": "SJT316", "Faculty": "SAHAAYA ARUL MARY S A"},
        {"Slot": "L31+L32", "Location": "SJT516", "Faculty": "VETRISELVI T"},
        {"Slot": "L33+L34", "Location": "SJT516", "Faculty": "KALAIVANI K"},
        {"Slot": "L49+L50", "Location": "SJT316", "Faculty": "KANNADASAN R"},
        {"Slot": "L51+L52", "Location": "SJT316", "Faculty": "VISHNUPRIYA"},
        {"Slot": "L49+L50", "Location": "SJT516", "Faculty": "BHUVANESWARI M"},
        {"Slot": "L33+L34", "Location": "SJT316", "Faculty": "KANAGARAJ R"},
        {"Slot": "L43+L44", "Location": "SJT316", "Faculty": "DEBI PRASANNA ACHARJYA"},
        {"Slot": "L33+L34", "Location": "SJT319", "Faculty": "SABYASACHI KAMILA"},
        {"Slot": "L51+L52", "Location": "SJT516", "Faculty": "SATHYA K"},
        {"Slot": "L31+L32", "Location": "SJT318", "Faculty": "ISLABUDEEN M"},
        {"Slot": "L35+L36", "Location": "SJT516", "Faculty": "SUGANTHINI C"},
        {"Slot": "L35+L36", "Location": "SJT316", "Faculty": "BASKARAN P"},
        {"Slot": "L45+L46", "Location": "SJT316", "Faculty": "UMA PRIYA D"},
        {"Slot": "L37+L38", "Location": "SJT316", "Faculty": "BAIJU B V"},
        {"Slot": "L53+L54", "Location": "SJT316", "Faculty": "MUKKU NISANTH KARTHEEK"},
        {"Slot": "L51+L52", "Location": "SJT318", "Faculty": "ARUMUGA ARUN R"},
        {"Slot": "L49+L50", "Location": "SJT319", "Faculty": "NAGA PRIYADARSHINI R"},
        {"Slot": "L31+L32", "Location": "SJT416", "Faculty": "BHAWANA TYAGI"}
    ],
    "Database Systems": [
        {"Slot": "A1+TA1", "Location": "SJT501", "Faculty": "GEETHA MARY A"},
        {"Slot": "A1+TA1", "Location": "SJT604", "Faculty": "SARASWATHI PRIYADHARSHINI A"},
        {"Slot": "A1+TA1", "Location": "SJT703", "Faculty": "JEEVANAJYOTHI PUJARI"},
        {"Slot": "A1+TA1", "Location": "SJT712", "Faculty": "RAMANATHAN L"},
        {"Slot": "A1+TA1", "Location": "SJT508", "Faculty": "AKILA VECTOR"},
        {"Slot": "A1+TA1", "Location": "SJT503", "Faculty": "RAJASHKANNAN R"},
        {"Slot": "A1+TA1", "Location": "SJT504", "Faculty": "SHASHANK MOULI SATAPATHY"},
        {"Slot": "A1+TA1", "Location": "SJT521", "Faculty": "JOSHVA DEVADAS T"},
        {"Slot": "A1+TA1", "Location": "SJT522", "Faculty": "ILAYARAJA V"},
        {"Slot": "A1+TA1", "Location": "SJT505", "Faculty": "NAVAMANI T M"},
        {"Slot": "A1+TA1", "Location": "SJT513", "Faculty": "JYOTISMITA CHAKI"},
        {"Slot": "A1+TA1", "Location": "SJT601", "Faculty": "ANBARASI M"},
        {"Slot": "A1+TA1", "Location": "SJT602A", "Faculty": "LYDIA JANE G"},
        {"Slot": "A1+TA1", "Location": "SJT626", "Faculty": "POORNIMA N"},
        {"Slot": "A1+TA1", "Location": "SJT627", "Faculty": "KONATHAM SUMALATHA"},
        {"Slot": "A1+TA1", "Location": "SJT702", "Faculty": "MOHAN KUMAR P"},
        {"Slot": "A1+TA1", "Location": "SJT707", "Faculty": "KRISHNA RANI SAMAL K"},
        {"Slot": "A1+TA1", "Location": "SJT704", "Faculty": "SRIDEVI S"},
        {"Slot": "A1+TA1", "Location": "SJT709", "Faculty": "PRIYADHARSHINI M"},
        {"Slot": "A1+TA1", "Location": "SJT710", "Faculty": "KARTHIK K"},
        {"Slot": "A1+TA1", "Location": "SJT711", "Faculty": "ANAND BIHARI"},
        {"Slot": "A1+TA1", "Location": "SJT502", "Faculty": "SAWTHI J.N"}
    ],
    "Database Systems Lab": [
        {"Slot": "L49+L50", "Location": "SJT416", "Faculty": "GEETHA MARY A"},
        {"Slot": "L55+L56", "Location": "SJT319", "Faculty": "SARAWATHI PRIYADARSHINI A"},
        {"Slot": "L49+L50", "Location": "SJT418", "Faculty": "JEEVANAJYOTHI PUJARI"},
        {"Slot": "L51+L52", "Location": "SJT416", "Faculty": "RAMANATHAN L"},
        {"Slot": "L39+L40", "Location": "SJT416", "Faculty": "AKILA VECTOR"},
        {"Slot": "L33+L34", "Location": "SJT417", "Faculty": "RAJASHKANNAN R"},
        {"Slot": "L33+L34", "Location": "SJT416", "Faculty": "SHASHANK MOULI SATAPATHY"},
        {"Slot": "L53+L54", "Location": "SJT417", "Faculty": "JOSHVA DEVDAS T"},
        {"Slot": "L39+L40", "Location": "SJT417", "Faculty": "ILAYARAJA V"},
        {"Slot": "L49+L50", "Location": "SJT417", "Faculty": "NAVAMANI T M"},
        {"Slot": "L45+L46", "Location": "SJT417", "Faculty": "JYOTISMITA CHAKI"},
        {"Slot": "L45+L46", "Location": "SJT416", "Faculty": "ANBARASI M"},
        {"Slot": "L37+L38", "Location": "SJT417", "Faculty": "LYDIA JANE G"},
        {"Slot": "L41+L42", "Location": "SJT417", "Faculty": "POORNIMA N"},
        {"Slot": "L37+L38", "Location": "SJT416", "Faculty": "KONTHAM SUMALATHA"},
        {"Slot": "L41+L42", "Location": "SJT416", "Faculty": "MOHAN KUMAR P"},
        {"Slot": "L47+L48", "Location": "SJT417", "Faculty": "KRISHNA RANI SAMAL K"},
        {"Slot": "L49+L50", "Location": "ST419", "Faculty": "SRIDEVI S"},
        {"Slot": "L47+L48", "Location": "SJT416", "Faculty": "PRIYADHARSHINI M"},
        {"Slot": "L33+L34", "Location": "SJT418", "Faculty": "KARTHIK K"},
        {"Slot": "L33+L34", "Location": "SJT419", "Faculty": "ANAND BIHARI"},
        {"Slot": "L31+L32", "Location": "SJT417", "Faculty": "SWATHI J.N"}
    ],
    "Computer Networks Lab": [
        {"Slot": "L51+L52", "Location": "SJT418", "Faculty": "SALEEM DURAI M.A"},
        {"Slot": "L37+L38", "Location": "SJT418", "Faculty": "SANTHI H"},
        {"Slot": "L57+L58", "Location": "SJT418", "Faculty": "YOKESH BABU S"},
        {"Slot": "L39+L40", "Location": "SJT419", "Faculty": "ANAND KUMAR S"},
        {"Slot": "L43+L44", "Location": "SJT418", "Faculty": "MANIKANDAN G"},
        {"Slot": "L57+L58", "Location": "SJT419", "Faculty": "SARWESH P"},
        {"Slot": "L43+L44", "Location": "SJT416", "Faculty": "TAMIZHSELVI SP"},
        {"Slot": "L31+L32", "Location": "SJT419", "Faculty": "UMADEVI K S"},
        {"Slot": "L35+L36", "Location": "SJT419", "Faculty": "THAMIZHARASAN S"},
        {"Slot": "L35+L36", "Location": "SJT418", "Faculty": "CHANDRU VIGNESH C"},
        {"Slot": "L55+L56", "Location": "SJT416", "Faculty": "KOPPERUNDEVI N"},
        {"Slot": "L41+L42", "Location": "SJT621", "Faculty": "KOVENDAN A.K.P"},
        {"Slot": "L43+L44", "Location": "SJT417", "Faculty": "SIVAKUMAR V"},
        {"Slot": "L59+L60", "Location": "SJT419", "Faculty": "KAMANASISH BHATTACHARJEE"},
        {"Slot": "L37+L38", "Location": "SJT419", "Faculty": "TAMIZHARASI T"},
        {"Slot": "L39+L40", "Location": "SJT418", "Faculty": "JAYAKUMAR K"},
        {"Slot": "L41+L42", "Location": "SJT419", "Faculty": "SREETHAR S"},
        {"Slot": "L43+L44", "Location": "SJT419", "Faculty": "SURESH A"},
        {"Slot": "L31+L32", "Location": "SJT418", "Faculty": "ARIVOLI A"},
        {"Slot": "L51+L52", "Location": "SJT419", "Faculty": "DILIPKUMAR S"},
        {"Slot": "L55+L56", "Location": "SJT417", "Faculty": "SASIKALA .R"}
    ],
    "Computer Networks": [
        {"Slot": "D1+TD1", "Location": "SJT501", "Faculty": "SALEEM DURAI M.A"},
        {"Slot": "D1+TD1", "Location": "SJT503", "Faculty": "SANTHI H"},
        {"Slot": "D1+TD1", "Location": "SJT505", "Faculty": "YOKESH BABU S"},
        {"Slot": "D1+TD1", "Location": "SJT504", "Faculty": "ANAND KUMAR S"},
        {"Slot": "D1+TD1", "Location": "SJT7601", "Faculty": "MANIKANDAN G"},
        {"Slot": "D1+TD1", "Location": "SJT602A", "Faculty": "SARWESH P"},
        {"Slot": "D1+TD1", "Location": "SJT707", "Faculty": "TAMIZHSELVI SP"},
        {"Slot": "D1+TD1", "Location": "SJT323", "Faculty": "UMADEVI K S"},
        {"Slot": "D1+TD1", "Location": "SJT627", "Faculty": "THAMIZHARASAN S"},
        {"Slot": "D1+TD1", "Location": "SJT702", "Faculty": "CHANDRU VIGNESH C"},
        {"Slot": "D1+TD1", "Location": "SJT703", "Faculty": "KOPPERUNDEVI N"},
        {"Slot": "D1+TD1", "Location": "SJT704", "Faculty": "KOVENDAN A.K.P"},
        {"Slot": "D1+TD1", "Location": "SJT709", "Faculty": "SIVAKUMAR V"},
        {"Slot": "D1+TD1", "Location": "SJT710", "Faculty": "KAMANASISH BHATTACHARJEE"},
        {"Slot": "D1+TD1", "Location": "SJT508", "Faculty": "TAMIZHARASI T"},
        {"Slot": "D1+TD1", "Location": "SJT513", "Faculty": "JAYAKUMAR K"},
        {"Slot": "D1+TD1", "Location": "SJT521", "Faculty": "SREETHAR S"},
        {"Slot": "D1+TD1", "Location": "SJT603", "Faculty": "SURESH A"},
        {"Slot": "D1+TD1", "Location": "SJT604", "Faculty": "ARIVOLI A"},
        {"Slot": "D1+TD1", "Location": "SJT626", "Faculty": "DILIPKUMAR S"},
        {"Slot": "D1+TDI", "Location": "SJT712", "Faculty": "SASIKALA .R"}
    ],
    "Operating Systems Lab": [
        {"Slot": "L31+L32", "Location": "SJT317", "Faculty": "ANISHA M.LAL"},
        {"Slot": "L55+L56", "Location": "SJT317", "Faculty": "SENDHIL KUMAR K.S."},
        {"Slot": "L45+L46", "Location": "SJT317", "Faculty": "SIVAKUMAR N"},
        {"Slot": "L47+L48", "Location": "SJT317", "Faculty": "NARAYAN PRASANTH"},
        {"Slot": "L43+L44", "Location": "SJT317", "Faculty": "KUMARESAN A"},
        {"Slot": "L39+L40", "Location": "SJT317", "Faculty": "ANTO S"},
        {"Slot": "L47+L48", "Location": "SJT319", "Faculty": "SIVAPRAKASH S"},
        {"Slot": "L45+L46", "Location": "SJT319", "Faculty": "PERPI RAJARAJESWARI"},
        {"Slot": "L45+L46", "Location": "SJT318", "Faculty": "SURESH P"},
        {"Slot": "L31+L32", "Location": "SJT319", "Faculty": "NAVEENKUMAR J"},
        {"Slot": "L57+L58", "Location": "SJT515", "Faculty": "BHULAKSHMI BONTHU"},
        {"Slot": "L53+L54", "Location": "SJT319", "Faculty": "DEEPA.K"},
        {"Slot": "L53+L54", "Location": "SJT317", "Faculty": "USHUS ELIZEBETH ZACHARIAH"},
        {"Slot": "L57+L58", "Location": "SJT319", "Faculty": "RUBY D"},
        {"Slot": "L57+L58", "Location": "SJT317", "Faculty": "HITESHWAR KUMAR AZAD"},
        {"Slot": "L59+L60", "Location": "SJT317", "Faculty": "NIHA K"},
        {"Slot": "L51+L52", "Location": "SJT319", "Faculty": "BALAJI N"},
        {"Slot": "L39+L40", "Location": "SJT319", "Faculty": "MOHANKUMAR B"},
        {"Slot": "L41+L42", "Location": "SJT317", "Faculty": "YOGANAND S"},
        {"Slot": "L47+L48", "Location": "SJT316", "Faculty": "EZHIL ARASI V"},
        {"Slot": "L55+L56", "Location": "SJT318", "Faculty": "MALINI S"},
        {"Slot": "L59+L60", "Location": "SJT318", "Faculty": "RAHUL SRIVASTAVA"},
        {"Slot": "L33+L34", "Location": "SJT317", "Faculty": "PADMAVATHY T"}
    ],
    "Sts": [
        {"Slot": "G1+TG1", "Location": "SJT101", "Faculty": "Face"},
    ]
}

## For evening timetable

courses_details_evening = {
    "Artificial Intelligence": [
        {"Slot": "E2+TE2", "Location": "SJT501", "Faculty": "JAISHANKAR N"},
        {"Slot": " E2+TE2", "Location": "SJT502", "Faculty": "SARVANAGURU RA.K"},
        {"Slot": " E2+TE2", "Location": "SJT508", "Faculty": "AKILA VECTOR"},
        {"Slot": " E2+TE2", "Location": "SJT505", "Faculty": "NAGA RAJA G"},
        {"Slot": "E2 + TE2", "Location": "SJT513", "Faculty": "ILANTHERAL K P S K"},
        {"Slot": "E2 + TE2", "Location": "SJT603", "Faculty": "RISHIN HALDAR"},
        {"Slot": "E2 + TE2", "Location": "SJT503", "Faculty": "RAJAKUMAR K"},
        {"Slot": "E2 + TE2", "Location": "SJT504", "Faculty": "VISHWANATHAN P"},
        {"Slot": "E2 + TE2", "Location": "SJT522", "Faculty": "BALAMURGAN R"},
        {"Slot": "E2 + TE2", "Location": "SJT702", "Faculty": "SRIDHAR RAJ S"},
        {"Slot": "E2 + TE2", "Location": "SJT604", "Faculty": "JAYASHREE J"},
        {"Slot": "E2 + TE2", "Location": "SJT521", "Faculty": "NAVAMANI T M"},
        {"Slot": "E2 + TE2", "Location": "SJT601", "Faculty": "SUDARSHAN NANDY"},
        {"Slot": "E2 + TE2", "Location": "SJT707", "Faculty": "NAGA PRIYADARSHINI R"},
        {"Slot": "E2 + TE2", "Location": "SJT709", "Faculty": "MOHAN KUMAR P"},
        {"Slot": "E2 + TE2", "Location": "SJT626", "Faculty": "JAGALINGAM P"},
        {"Slot": "E2 + TE2", "Location": "SJT602 A", "Faculty": "SHALINI L"},
        {"Slot": "E2 + TE2", "Location": "SJT627", "Faculty": "MOHANA CM"},
        {"Slot": "E2 + TE2", "Location": "SJT703", "Faculty": "SUNIJA A P"},
        {"Slot": "E2 + TE2", "Location": "SJT704", "Faculty": "SAMRIDDHI SARKAR"},
        {"Slot": "E2 + TE2", "Location": "SJT710", "Faculty": "RAJAY VEDARAJ I.S"}
    ],
    "Operating Systems": [
        {"Slot": "B2 + TB2", "Location": "SJT508", "Faculty": "PERPI RAJARAJESWARI"},
        {"Slot": "B2 + TB2", "Location": "SJT513", "Faculty": "NAVEENKUMAR J"},
        {"Slot": "B2 + TB2", "Location": "SJT522", "Faculty": "BHULAKSHMI BONTHU"},
        {"Slot": "B2 + TB2", "Location": "SJT627", "Faculty": "SIVAPRAKASH S"},
        {"Slot": "B2 + TB2", "Location": "SJT702", "Faculty": "KUMARESAN A"},
        {"Slot": "B2 + TB2", "Location": "SJT501", "Faculty": "ANISHA M.LAL"},
        {"Slot": "B2 + TB2", "Location": "SJT503", "Faculty": "SENDHIL KUMAR K.S"},
        {"Slot": "B2 + TB2", "Location": "SJT502", "Faculty": "SIVAKUMAR N"},
        {"Slot": "B2 + TB2", "Location": "SJT504", "Faculty": "NARAYAN PRASANTH"},
        {"Slot": "B2 + TB2", "Location": "SJT505", "Faculty": "ANTO S"},
        {"Slot": "B2 + TB2", "Location": "SJT521", "Faculty": "SURESH P"},
        {"Slot": "B2 + TB2", "Location": "SJT602A", "Faculty": "DEEPA .K"},
        {"Slot": "B2 + TB2", "Location": "SJT601", "Faculty": "USHUS ELIZEBETH ZACHARIAH"},
        {"Slot": "B2 + TB2", "Location": "SJT603", "Faculty": "RUBY D"},
        {"Slot": "B2 + TB2", "Location": "SJT604", "Faculty": "HITESHWAR KUMAR AZAD"},
        {"Slot": "B2 + TB2", "Location": "SJT626", "Faculty": "NIHA K"},
        {"Slot": "B2 + TB2", "Location": "SJT704", "Faculty": "BALAJI N"},
        {"Slot": "B2 + TB2", "Location": "SJT709", "Faculty": "MOHANKUMAR B"},
        {"Slot": "B2 + TB2", "Location": "SJT707", "Faculty": "YOGANAND S"},
        {"Slot": "B2 + TB2", "Location": "SJT710", "Faculty": "EZHIL ARASI V"},
        {"Slot": "B2 + TB2", "Location": "SJT712", "Faculty": "PADMAVATHY T"},
        {"Slot": "B2 + TB2", "Location": "SJT703", "Faculty": "MALINI S"},
        {"Slot": "B2 + TB2", "Location": "SJT711", "Faculty": "RAHUL SRIVASTAVA"}
    ],
    "Aws Solutions Architect": [
        {"Slot": "F2 + TF2", "Location": "SJT601", "Faculty": "BALKRISHNAN P"},
        {"Slot": "F2 + TF2", "Location": "SJT602A", "Faculty": "JOTHI K R"},
        {"Slot": "F2 + TF2", "Location": "SJT604", "Faculty": "JUSTIN GOPINATH A"},
        {"Slot": "F2 + TF2", "Location": "SJT626", "Faculty": "KANAGARAJ R"},
        {"Slot": "F2 + TF2", "Location": "SJT627", "Faculty": "KARTHIK G M"},
        {"Slot": "F2 + TF2", "Location": "SJT702", "Faculty": "KOPPERUNDEVI N"},
        {"Slot": "F2 + TF2", "Location": "SJT703", "Faculty": "PARTHASARTHY G"},
        {"Slot": "F2 + TF2", "Location": "SJT704", "Faculty": "THURAI RANDIAN M"},
        {"Slot": "F2 + TF2", "Location": "SJT707", "Faculty": "UMAMAHESWARI M"},
        {"Slot": "F2 + TF2", "Location": "SJT710", "Faculty": "GOUTAM MAJUMDER"},
        {"Slot": "F2 + TF2", "Location": "SJT709", "Faculty": "KONATHAM SUMALATHA"},
        {"Slot": "F2 + TF2", "Location": "SJT501", "Faculty": "NARAYANAMOORTHI M"},
        {"Slot": "F2 + TF2", "Location": "SJT502", "Faculty": "GOVINDA K"},
        {"Slot": "F2 + TF2", "Location": "SJT503", "Faculty": "MYTHILI T"},
        {"Slot": "F2 + TF2", "Location": "SJT508", "Faculty": "SRIVANI A"},
        {"Slot": "F2 + TF2", "Location": "SJT505", "Faculty": "ARCHANA T"},
        {"Slot": "F2 + TF2", "Location": "SJT504", "Faculty": "ABDUL GAFFAR H"},
        {"Slot": "F2 + TF2", "Location": "SJT715", "Faculty": "SANJIBAN SEKHAR ROY"},
        {"Slot": "F2 + TF2", "Location": "SJT513", "Faculty": "SUDHA.S"},
        {"Slot": "F2 + TF2", "Location": "SJT521", "Faculty": "NARESH K"},
        {"Slot": "F2 + TF2", "Location": "SJT522", "Faculty": "GOPICHAND G"},
        {"Slot": "F2 + TF2", "Location": "SJT603", "Faculty": "VINILA JINNY"},
        {"Slot": "F2 + TF2", "Location": "SJT712", "Faculty": "PRIYA G"},
        {"Slot": "F2 + TF2", "Location": "SJT711", "Faculty": "JAYAKUMAR S"}
    ],
    "Compiler Design": [
        {"Slot": "C2 + TC2", "Location": "SJT521", "Faculty": "SATHYA K"},
        {"Slot": "C2 + TC2", "Location": "SJT703", "Faculty": "BHAVANA TYAGI"},
        {"Slot": "C2 + TC2", "Location": "SJT704", "Faculty": "DEBI PRASANNA ACHARJYA"},
        {"Slot": "C2 + TC2", "Location": "SJT501", "Faculty": "SAHAAYA ARUL MARY S A"},
        {"Slot": "C2 + TC2", "Location": "SJT502", "Faculty": "KANNADASAN R"},
        {"Slot": "C2 + TC2", "Location": "SJT513", "Faculty": "KALAIVANI K"},
        {"Slot": "C2 + TC2", "Location": "SJT503", "Faculty": "VISHNUPRIYA"},
        {"Slot": "C2 + TC2", "Location": "SJT504", "Faculty": "BHUVANESWARI M"},
        {"Slot": "C2 + TC2", "Location": "SJT505", "Faculty": "VETRISELVI T"},
        {"Slot": "C2 + TC2", "Location": "SJT508", "Faculty": "KANAGARAJ R"},
        {"Slot": "C2 + TC2", "Location": "SJT601", "Faculty": "SABYASACHI KAMILA"},
        {"Slot": "C2 + TC2", "Location": "SJT626", "Faculty": "ISLABUDEEN M"},
        {"Slot": "C2 + TC2", "Location": "SJT627", "Faculty": "SUGANTHINI C"},
        {"Slot": "C2 + TC2", "Location": "SJT522", "Faculty": "BASKARAN P"},
        {"Slot": "C2 + TC2", "Location": "SJT602A", "Faculty": "UMA PRIYA D"},
        {"Slot": "C2 + TC2", "Location": "SJT707", "Faculty": "BAIJU B V"},
        {"Slot": "C2 + TC2", "Location": "SJT315", "Faculty": "NAVEEN MISHRA"},
        {"Slot": "C2 + TC2", "Location": "SJT603", "Faculty": "MUKKU NISANTH KARTHEEK"},
        {"Slot": "C2 + TC2", "Location": "SJT604", "Faculty": "ARUMUGA ARUN R"},
        {"Slot": "C2 + TC2", "Location": "SJT702", "Faculty": "NAGA PRIYADARSHINI R"}
    ],
    "Compiler Design Lab": [
{"Slot": "L1+L2", "Location": "SJT316", "Faculty": "SAHAAYA ARUL MARY S A"},
{"Slot": "L1+L2", "Location": "SJT516", "Faculty": "VETRISELVI T"},
{"Slot": "L3+L4", "Location": "SJT516", "Faculty": "KALAIVANI K"},
{"Slot": "L19+L20", "Location": "SJT316", "Faculty": "KANNADASAN R"},
{"Slot": "L21+L22", "Location": "SJT316", "Faculty": "VISHNUPRIYA"},
{"Slot": "L19+L20", "Location": "SJT516", "Faculty": "BHUVANESWARI M"},
{"Slot": "L3+L4", "Location": "SJT316", "Faculty": "KANAGARAJ R"},
{"Slot": "L13+L14", "Location": "SJT316", "Faculty": "DEBI PRASANNA ACHARJYA"},
{"Slot": "L3+L4", "Location": "SJT319", "Faculty": "SABYASACHI KAMILA"},
{"Slot": "L21+L22", "Location": "SJT516", "Faculty": "SATHYA K"},
{"Slot": "L1+L2", "Location": "SJT318", "Faculty": "ISLABUDEEN M"},
{"Slot": "L5+L6", "Location": "SJT516", "Faculty": "SUGANTHINI C"},
{"Slot": "L5+L6", "Location": "SJT316", "Faculty": "BASKARAN P"},
{"Slot": "L15+L16", "Location": "SJT316", "Faculty": "UMA PRIYA D"},
{"Slot": "L7+L8", "Location": "SJT316", "Faculty": "BAIJU B V"},
{"Slot": "L23+L24", "Location": "SJT316", "Faculty": "MUKKU NISANTH KARTHEEK"},
{"Slot": "L21+L22", "Location": "SJT318", "Faculty": "ARUMUGA ARUN R"},
{"Slot": "L19+L20", "Location": "SJT319", "Faculty": "NAGA PRIYADARSHINI R"},
{"Slot": "L1+L2", "Location": "SJT416", "Faculty": "BHAWANA TYAGI"}
],
    "Database Systems": [
        {"Slot": "A2 + TA2", "Location": "SJT501", "Faculty": "GEETHA MARY A"},
        {"Slot": "A2 + TA2", "Location": "SJT604", "Faculty": "SARASWATHI PRIYADHARSHINI A"},
        {"Slot": "A2 + TA2", "Location": "SJT703", "Faculty": "JEEVANAJYOTHI PUJARI"},
        {"Slot": "A2 + TA2", "Location": "SJT712", "Faculty": "RAMANATHAN L"},
        {"Slot": "A2 + TA2", "Location": "SJT508", "Faculty": "AKILA VECTOR"},
        {"Slot": "A2 + TA2", "Location": "SJT503", "Faculty": "RAJASHKANNAN R"},
        {"Slot": "A2 + TA2", "Location": "SJT504", "Faculty": "SHASHANK MOULI SATAPATHY"},
        {"Slot": "A2 + TA2", "Location": "SJT521", "Faculty": "JOSHVA DEVADAS T"},
        {"Slot": "A2 + TA2", "Location": "SJT522", "Faculty": "ILAYARAJA V"},
        {"Slot": "A2 + TA2", "Location": "SJT505", "Faculty": "NAVAMANI T M"},
        {"Slot": "A2 + TA2", "Location": "SJT513", "Faculty": "JYOTISMITA CHAKI"},
        {"Slot": "A2 + TA2", "Location": "SJT601", "Faculty": "ANBARASI M"},
        {"Slot": "A2 + TA2", "Location": "SJT602A", "Faculty": "LYDIA JANE G"},
        {"Slot": "A2 + TA2", "Location": "SJT626", "Faculty": "POORNIMA N"},
        {"Slot": "A2 + TA2", "Location": "SJT627", "Faculty": "KONATHAM SUMALATHA"},
        {"Slot": "A2 + TA2", "Location": "SJT702", "Faculty": "MOHAN KUMAR P"},
        {"Slot": "A2 + TA2", "Location": "SJT707", "Faculty": "KRISHNA RANI SAMAL K"},
        {"Slot": "A2 + TA2", "Location": "SJT704", "Faculty": "SRIDEVI S"},
        {"Slot": "A2 + TA2", "Location": "SJT709", "Faculty": "PRIYADHARSHINI M"},
        {"Slot": "A2 + TA2", "Location": "SJT710", "Faculty": "KARTHIK K"},
        {"Slot": "A2 + TA2", "Location": "SJT711", "Faculty": "ANAND BIHARI"},
        {"Slot": "A2 + TA2", "Location": "SJT502", "Faculty": "SAWTHI J.N"}
    ],
    "Database Systems Lab": [
{"Slot": "L19+L20", "Location": "SJT416", "Faculty": "GEETHA MARY A"},
{"Slot": "L25+L26", "Location": "SJT319", "Faculty": "SARAWATHI PRIYADARSHINI A"},
{"Slot": "L19+L20", "Location": "SJT418", "Faculty": "JEEVANAJYOTHI PUJARI"},
{"Slot": "L21+L22", "Location": "SJT416", "Faculty": "RAMANATHAN L"},
{"Slot": "L9+L10", "Location": "SJT416", "Faculty": "AKILA VECTOR"},
{"Slot": "L3+L4", "Location": "SJT417", "Faculty": "RAJASHKANNAN R"},
{"Slot": "L3+L4", "Location": "SJT416", "Faculty": "SHASHANK MOULI SATAPATHY"},
{"Slot": "L23+L24", "Location": "SJT417", "Faculty": "JOSHVA DEVDAS T"},
{"Slot": "L9+L10", "Location": "SJT417", "Faculty": "ILAYARAJA V"},
{"Slot": "L19+L20", "Location": "SJT417", "Faculty": "NAVAMANI T M"},
{"Slot": "L15+L16", "Location": "SJT417", "Faculty": "JYOTISMITA CHAKI"},
{"Slot": "L15+L16", "Location": "SJT416", "Faculty": "ANBARASI M"},
{"Slot": "L7+L8", "Location": "SJT417", "Faculty": "LYDIA JANE G"},
{"Slot": "L11+L12", "Location": "SJT417", "Faculty": "POORNIMA N"},
{"Slot": "L7+L8", "Location": "SJT416", "Faculty": "KONTHAM SUMALATHA"},
{"Slot": "L11+L12", "Location": "SJT416", "Faculty": "MOHAN KUMAR P"},
{"Slot": "L17+L18", "Location": "SJT417", "Faculty": "KRISHNA RANI SAMAL K"},
{"Slot": "L19+L20", "Location": "ST419", "Faculty": "SRIDEVI S"},
{"Slot": "L17+L18", "Location": "SJT416", "Faculty": "PRIYADHARSHINI M"},
{"Slot": "L3+L4", "Location": "SJT418", "Faculty": "KARTHIK K"},
{"Slot": "L3+L4", "Location": "SJT419", "Faculty": "ANAND BIHARI"},
{"Slot": "L1+L2", "Location": "SJT417", "Faculty": "SWATHI J.N"}
],
"Computer Networks Lab": [
{"Slot": "L21+L22", "Location": "SJT418", "Faculty": "SALEEM DURAI M.A"},
{"Slot": "L7+L8", "Location": "SJT418", "Faculty": "SANTHI H"},
{"Slot": "L27+L28", "Location": "SJT418", "Faculty": "YOKESH BABU S"},
{"Slot": "L9+L10", "Location": "SJT419", "Faculty": "ANAND KUMAR S"},
{"Slot": "L13+L14", "Location": "SJT418", "Faculty": "MANIKANDAN G"},
{"Slot": "L27+L28", "Location": "SJT419", "Faculty": "SARWESH P"},
{"Slot": "L13+L14", "Location": "SJT416", "Faculty": "TAMIZHSELVI SP"},
{"Slot": "L1+L2", "Location": "SJT419", "Faculty": "UMADEVI K S"},
{"Slot": "L5+L6", "Location": "SJT419", "Faculty": "THAMIZHARASAN S"},
{"Slot": "L5+L6", "Location": "SJT418", "Faculty": "CHANDRU VIGNESH C"},
{"Slot": "L25+L26", "Location": "SJT416", "Faculty": "KOPPERUNDEVI N"},
{"Slot": "L11+L12", "Location": "SJT621", "Faculty": "KOVENDAN A.K.P"},
{"Slot": "L13+L14", "Location": "SJT417", "Faculty": "SIVAKUMAR V"},
{"Slot": "L29+L30", "Location": "SJT419", "Faculty": "KAMANASISH BHATTACHARJEE"},
{"Slot": "L7+L8", "Location": "SJT419", "Faculty": "TAMIZHARASI T"},
{"Slot": "L9+L10", "Location": "SJT418", "Faculty": "JAYAKUMAR K"},
{"Slot": "L11+L12", "Location": "SJT419", "Faculty": "SREETHAR S"},
{"Slot": "L13+L14", "Location": "SJT419", "Faculty": "SURESH A"},
{"Slot": "L1+L2", "Location": "SJT418", "Faculty": "ARIVOLI A"},
{"Slot": "L21+L22", "Location": "SJT419", "Faculty": "DILIPKUMAR S"},
{"Slot": "L25+L26", "Location": "SJT417", "Faculty": "SASIKALA .R"}
],
    "Computer Networks": [
        {"Slot": "D2 + TD2", "Location": "SJT501", "Faculty": "SALEEM DURAI M.A"},
        {"Slot": "D2 + TD2", "Location": "SJT503", "Faculty": "SANTHI H"},
        {"Slot": "D2 + TD2", "Location": "SJT505", "Faculty": "YOKESH BABU S"},
        {"Slot": "D2 + TD2", "Location": "SJT504", "Faculty": "ANAND KUMAR S"},
        {"Slot": "D2 + TD2", "Location": "SJT7601", "Faculty": "MANIKANDAN G"},
        {"Slot": "D2 + TD2", "Location": "SJT602A", "Faculty": "SARWESH P"},
        {"Slot": "D2 + TD2", "Location": "SJT707", "Faculty": "TAMIZHSELVI SP"},
        {"Slot": "D2 + TD2", "Location": "SJT323", "Faculty": "UMADEVI K S"},
        {"Slot": "D2 + TD2", "Location": "SJT627", "Faculty": "THAMIZHARASAN S"},
        {"Slot": "D2 + TD2", "Location": "SJT702", "Faculty": "CHANDRU VIGNESH C"},
        {"Slot": "D2 + TD2", "Location": "SJT703", "Faculty": "KOPPERUNDEVI N"},
        {"Slot": "D2 + TD2", "Location": "SJT704", "Faculty": "KOVENDAN A.K.P"},
        {"Slot": "D2 + TD2", "Location": "SJT709", "Faculty": "SIVAKUMAR V"},
        {"Slot": "D2 + TD2", "Location": "SJT710", "Faculty": "KAMANASISH BHATTACHARJEE"},
        {"Slot": "D2 + TD2", "Location": "SJT508", "Faculty": "TAMIZHARASI T"},
        {"Slot": "D2 + TD2", "Location": "SJT513", "Faculty": "JAYAKUMAR K"},
        {"Slot": "D2 + TD2", "Location": "SJT521", "Faculty": "SREETHAR S"},
        {"Slot": "D2 + TD2", "Location": "SJT603", "Faculty": "SURESH A"},
        {"Slot": "D2 + TD2", "Location": "SJT604", "Faculty": "ARIVOLI A"},
        {"Slot": "D2 + TD2", "Location": "SJT626", "Faculty": "DILIPKUMAR S"},
        {"Slot": "D1+TDI", "Location": "SJT712", "Faculty": "SASIKALA .R"}
    ],
    "Operating Systems Lab": [
{"Slot": "L1+L2", "Location": "SJT317", "Faculty": "ANISHA M.LAL"},
{"Slot": "L25+L26", "Location": "SJT317", "Faculty": "SENDHIL KUMAR K.S."},
{"Slot": "L15+L16", "Location": "SJT317", "Faculty": "SIVAKUMAR N"},
{"Slot": "L17+L18", "Location": "SJT317", "Faculty": "NARAYAN PRASANTH"},
{"Slot": "L13+L14", "Location": "SJT317", "Faculty": "KUMARESAN A"},
{"Slot": "L9+L10", "Location": "SJT317", "Faculty": "ANTO S"},
{"Slot": "L17+L18", "Location": "SJT319", "Faculty": "SIVAPRAKASH S"},
{"Slot": "L15+L16", "Location": "SJT319", "Faculty": "PERPI RAJARAJESWARI"},
{"Slot": "L15+L16", "Location": "SJT318", "Faculty": "SURESH P"},
{"Slot": "L1+L2", "Location": "SJT319", "Faculty": "NAVEENKUMAR J"},
{"Slot": "L27+L28", "Location": "SJT515", "Faculty": "BHULAKSHMI BONTHU"},
{"Slot": "L23+L24", "Location": "SJT319", "Faculty": "DEEPA.K"},
{"Slot": "L23+L24", "Location": "SJT317", "Faculty": "USHUS ELIZEBETH ZACHARIAH"},
{"Slot": "L27+L28", "Location": "SJT319", "Faculty": "RUBY D"},
{"Slot": "L27+L28", "Location": "SJT317", "Faculty": "HITESHWAR KUMAR AZAD"},
{"Slot": "L29+L30", "Location": "SJT317", "Faculty": "NIHA K"},
{"Slot": "L21+L22", "Location": "SJT319", "Faculty": "BALAJI N"},
{"Slot": "L9+L10", "Location": "SJT319", "Faculty": "MOHANKUMAR B"},
{"Slot": "L11+L12", "Location": "SJT317", "Faculty": "YOGANAND S"},
{"Slot": "L17+L18", "Location": "SJT316", "Faculty": "EZHIL ARASI V"},
{"Slot": "L25+L26", "Location": "SJT318", "Faculty": "MALINI S"},
{"Slot": "L29+L30", "Location": "SJT318", "Faculty": "RAHUL SRIVASTAVA"},
{"Slot": "L3+L4", "Location": "SJT317", "Faculty": "PADMAVATHY T"}
],
 "Sts": [
        {"Slot": "G2+TG2", "Location": "SJT101", "Faculty": "Face"},
    ]
}


# Theory slot timings with multiple entries per slot
THEORY_SLOTS_MORNING = {
    #Morning slots
    

    'A1': [('MON', '08:00', '08:50'), ('WED', '09:00', '09:50')],
    'TA1': [('FRI', '10:00', '10:50')],
    'B1': [('TUE', '08:00', '08:50'), ('THU', '09:00', '09:50')],
    'TB1': [('MON', '11:00', '11:50')],
    'C1': [('WED', '08:00', '08:50'), ('FRI', '09:00', '09:50')],
    'TC1': [('TUE', '11:00', '11:50')],
    'D1': [('THU', '08:00', '08:50'), ('MON', '10:00', '10:50')],
    'TD1': [('FRI', '12:00', '12:50')],
    'E1': [('FRI', '08:00', '08:50'), ('TUE', '10:00', '10:50')],
    'TE1': [('THU', '11:00', '11:50')],
    'F1': [('MON', '09:00', '09:50'), ('WED', '10:00', '10:50')],
    'TF1': [('FRI', '11:00', '11:50')],
    'G1': [('TUE', '09:00', '09:50'), ('THU', '10:00', '10:50')],
    'TG1': [('MON', '12:00', '12:50')],
    
}
    # Evening slots
THEORY_SLOTS_EVENING={


    'A2': [('MON', '14:00', '14:50'), ('THU', '17:00', '17:50')],
    'TA2': [('FRI', '16:00', '16:50')],
    'B2': [('WED', '14:00', '14:50'), ('THU', '18:00', '18:50')],
    'TB2': [('FRI', '17:00', '17:50')],
    'C2': [('THU', '14:00', '14:50'), ('FRI', '18:00', '18:50')],
    'TC2': [('WED', '17:00', '17:50')],
    'D2': [('MON', '16:00', '16:50'), ('FRI', '14:00', '14:50')],
    'TD2': [('THU', '19:00', '19:50')],
    'E2': [('TUE', '16:00', '16:50'), ('FRI', '14:00', '14:50')],
    'TE2': [('THU', '17:00', '17:50')],
    'F2': [('MON', '17:00', '17:50'), ('WED', '16:00', '16:50')],
    'TF2': [('THU', '15:00', '15:50')],
    'G2': [('MON', '15:00', '15:50'), ('FRI', '16:00', '16:50')],
    'TG2': [('WED', '18:00', '18:50')]
    
}

# Lab slot timings (L1-L60)
LAB_SLOTS_Morning = {

    


    # MONDAY MORNING
    'L1': ('MON', '08:00', '08:50'),
    'L2': ('MON', '08:51', '09:40'),
    'L3': ('MON', '09:51', '10:40'),
    'L4': ('MON', '10:41', '11:30'),
    'L5': ('MON', '11:40', '12:30'),
    'L6': ('MON', '12:31', '13:20'),

    # TUESDAY MORNING
    'L7': ('TUE', '08:00', '08:50'),
    'L8': ('TUE', '08:51', '09:40'),
    'L9': ('TUE', '09:51', '10:40'),
    'L10': ('TUE', '10:41', '11:30'),
    'L11': ('TUE', '11:40', '12:30'),
    'L12': ('TUE', '12:31', '13:20'),

    # WEDNESDAY MORNING
    'L13': ('WED', '08:00', '08:50'),
    'L14': ('WED', '08:51', '09:40'),
    'L15': ('WED', '09:51', '10:40'),
    'L16': ('WED', '10:41', '11:30'),
    'L17': ('WED', '11:40', '12:30'),
    'L18': ('WED', '12:31', '13:20'),

    # THURSDAY MORNING
    'L19': ('THU', '08:00', '08:50'),
    'L20': ('THU', '08:51', '09:40'),
    'L21': ('THU', '09:51', '10:40'),
    'L22': ('THU', '10:41', '11:30'),
    'L23': ('THU', '11:40', '12:30'),
    'L24': ('THU', '12:31', '13:20'),

    # FRIDAY MORNING
    'L25': ('FRI', '08:00', '08:50'),
    'L26': ('FRI', '08:51', '09:40'),
    'L27': ('FRI', '09:51', '10:40'),
    'L28': ('FRI', '10:41', '11:30'),
    'L29': ('FRI', '11:40', '12:30'),
    'L30': ('FRI', '12:31', '13:20'),
    
}
LAB_SLOTS_EVENING ={

    # MONDAY AFTERNOON
    'L31': ('MON', '14:00', '14:50'),
    'L32': ('MON', '14:51', '15:40'),
    'L33': ('MON', '15:51', '16:40'),
    'L34': ('MON', '16:41', '17:30'),
    'L35': ('MON', '17:40', '18:30'),
    'L36': ('MON', '18:31', '19:20'),

    # TUESDAY AFTERNOON
    'L37': ('TUE', '14:00', '14:50'),
    'L38': ('TUE', '14:51', '15:40'),
    'L39': ('TUE', '15:51', '16:40'),
    'L40': ('TUE', '16:41', '17:30'),
    'L41': ('TUE', '17:40', '18:30'),
    'L42': ('TUE', '18:31', '19:20'),

    # WEDNESDAY AFTERNOON
    'L43': ('WED', '14:00', '14:50'),
    'L44': ('WED', '14:51', '15:40'),
    'L45': ('WED', '15:51', '16:40'),
    'L46': ('WED', '16:41', '17:30'),
    'L47': ('WED', '17:40', '18:30'),
    'L48': ('WED', '18:31', '19:20'),

    # THURSDAY AFTERNOON
    'L49': ('THU', '14:00', '14:50'),
    'L50': ('THU', '14:51', '15:40'),
    'L51': ('THU', '15:51', '16:40'),
    'L52': ('THU', '16:41', '17:30'),
    'L53': ('THU', '17:40', '18:30'),
    'L54': ('THU', '18:31', '19:20'),

    # FRIDAY AFTERNOON
    'L55': ('FRI', '14:00', '14:50'),
    'L56': ('FRI', '14:51', '15:40'),
    'L57': ('FRI', '15:51', '16:40'),
    'L58': ('FRI', '16:41', '17:30'),
    'L59': ('FRI', '17:40', '18:30'),
    'L60': ('FRI', '18:31', '19:20'),
        
}

# Map lab courses to their corresponding theory courses
LAB_TO_THEORY = {
    'OPERATING SYSTEMS LAB': 'OPERATING SYSTEMS',
    'COMPILER DESIGN LAB': 'COMPILER DESIGN',
    'DATABASE SYSTEMS LAB': 'DATABASE SYSTEMS',
    'COMPUTER NETWORKS LAB': 'COMPUTER NETWORKS'
}




        



# Function to convert time to minutes
def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

# Parse times for the slots
def parse_slot_times(slot_names):
    times = []
    for slot_name in slot_names:
        if slot_name in THEORY_SLOTS:
            for day, start, end in THEORY_SLOTS[slot_name]:
                times.append((day, start, end))
        elif slot_name in LAB_SLOTS:
            day, start, end = LAB_SLOTS[slot_name]
            times.append((day, start, end))
        else:
            print(f"Slot {slot_name} not found in THEORY_SLOTS or LAB_SLOTS.")
    return times

# Check for time overlap
def times_overlap(t1_start, t1_end, t2_start, t2_end):
    return max(t1_start, t2_start) < min(t1_end, t2_end)

# Check for schedule conflicts
def schedule_conflict(schedule, new_times):
    for day, start, end in new_times:
        start_min = time_to_minutes(start)
        end_min = time_to_minutes(end)
        for existing_start, existing_end in schedule.get(day, []):
            existing_start_min = time_to_minutes(existing_start)
            existing_end_min = time_to_minutes(existing_end)
            if times_overlap(start_min, end_min, existing_start_min, existing_end_min):
                return True
    return False

# Add to schedule
def add_to_schedule(schedule, times):
    for day, start, end in times:
        if day not in schedule:
            schedule[day] = []
        schedule[day].append((start, end))

# Remove from schedule
def remove_from_schedule(schedule, times):
    for day, start, end in times:
        schedule[day].remove((start, end))
        if not schedule[day]:
            del schedule[day]

# Compute gaps
def compute_gaps(schedule):
    total_gaps = 0
    for day in schedule:
        times = schedule[day]
        intervals = sorted([(time_to_minutes(start), time_to_minutes(end)) for start, end in times])
        for i in range(len(intervals) - 1):
            gap = intervals[i+1][0] - intervals[i][1]
            total_gaps += gap // 10
    return total_gaps

# Check if a slot is in the desired time (morning/evening)
def slot_in_time(slot_option, desired_time):
    slot_names = slot_option.split('+')
    times = parse_slot_times(slot_names)
    for _, start, _ in times:
        start_min = time_to_minutes(start)
        if desired_time == 'morning':
            if start_min >= 840:  # 14:00 in minutes
                return False
        elif desired_time == 'evening':
            if start_min < 840:
                return False
    return True

# Generate the initial timetable
def generate_initial_timetable():
    for theory_time in ['morning', 'evening']:
        lab_time = 'evening' if theory_time == 'morning' else 'morning'
        timetable = {}
        schedule = {}
        failed = False
        
        # Schedule theory courses
        theory_courses = [course for course in COURSES if course not in LAB_TO_THEORY]
        for course in theory_courses:
            slot_options = [opt for opt in COURSES[course] if slot_in_time(opt, theory_time)]
            if not slot_options:
                failed = True
                break
            random.shuffle(slot_options)
            for slot_option in slot_options:
                times = parse_slot_times(slot_option.split('+'))
                if not schedule_conflict(schedule, times):
                    timetable[course] = slot_option
                    add_to_schedule(schedule, times)
                    break
            else:
                failed = True
                break
        
        if failed:
            continue  # Try the other theory_time

        # Schedule lab courses
        lab_courses = [course for course in COURSES if course in LAB_TO_THEORY]
        for course in lab_courses:
            slot_options = [opt for opt in COURSES[course] if slot_in_time(opt, lab_time)]
            if not slot_options:
                failed = True
                break
            random.shuffle(slot_options)
            for slot_option in slot_options:
                times = parse_slot_times(slot_option.split('+'))
                if not schedule_conflict(schedule, times):
                    timetable[course] = slot_option
                    add_to_schedule(schedule, times)
                    break
            else:
                failed = True
                break
        
        if not failed:
            return timetable, schedule
    
    return None, None

# Hill climbing optimization
def hill_climbing(timetable, schedule):
    current_timetable = copy.deepcopy(timetable)
    current_schedule = copy.deepcopy(schedule)
    current_cost = compute_gaps(current_schedule)
    print(f"Initial number of 10-minute gaps: {current_cost}")
    iteration = 0
    while True:
        neighbors = []
        for course in current_timetable:
            if len(COURSES[course]) <= 1:
                continue
            current_slot_option = current_timetable[course]
            for slot_option in COURSES[course]:
                if slot_option != current_slot_option:
                    if course in LAB_TO_THEORY:
                        theory_course = LAB_TO_THEORY[course]
                        theory_slot_option = current_timetable[theory_course]
                        if slot_in_time(theory_slot_option, 'morning'):
                            desired_lab_time = 'evening'
                        else:
                            desired_lab_time = 'morning'
                        if not slot_in_time(slot_option, desired_lab_time):
                            continue
                    else:
                        if not slot_in_time(slot_option, 'morning') and not slot_in_time(slot_option, 'evening'):
                            continue
                    new_timetable = copy.deepcopy(current_timetable)
                    new_schedule = copy.deepcopy(current_schedule)
                    old_times = parse_slot_times(current_slot_option.split('+'))
                    remove_from_schedule(new_schedule, old_times)
                    new_times = parse_slot_times(slot_option.split('+'))
                    if not schedule_conflict(new_schedule, new_times):
                        new_timetable[course] = slot_option
                        add_to_schedule(new_schedule, new_times)
                        cost = compute_gaps(new_schedule)
                        neighbors.append((cost, new_timetable, new_schedule))
        if not neighbors:
            break
        neighbors.sort(key=lambda x: x[0])
        best_neighbor = neighbors[0]
        if best_neighbor[0] < current_cost:
            current_cost = best_neighbor[0]
            current_timetable = best_neighbor[1]
            current_schedule = best_neighbor[2]
            iteration += 1
            print(f"Iteration {iteration}: Number of 10-minute gaps: {current_cost}")
        else:
            break
    return current_timetable, current_schedule

# Display timetable with slot details
def print_slot_based_timetable(timetable, courses_details):
    print("\nSlot-based Timetable with Location and Faculty:")
    for course, slot_option in timetable.items():
        course_details = courses_details.get(course.replace('_', ' ').title(), [])
        for detail in course_details:
            if detail['Slot'] == slot_option:
                location = detail['Location']
                faculty = detail['Faculty']
                print(f"{course.replace('_', ' ').title()}: Slot: {slot_option}, Location: {location}, Faculty: {faculty}")
                break
        else:
            print(f"{course.replace('_', ' ').title()}: Slot: {slot_option} (Details not found)")
    print("\n")

x = input()

if(x == "Morning"):
    COURSES = Course_Morning
    courses_details = courses_details_morning
    THEORY_SLOTS = THEORY_SLOTS_MORNING
    LAB_SLOTS = LAB_SLOTS_Morning
elif(x == "Evening"):
    COURSES = Course_Evening
    course_details = courses_details_evening
    THEORY_SLOTS = THEORY_SLOTS_EVENING
    LAB_SLOTS = LAB_SLOTS_EVENING

# Generate and print the initial timetable
timetable, schedule = generate_initial_timetable()
if timetable:
    print("Initial Timetable (Slot-based):")
    print_slot_based_timetable(timetable, courses_details)

    # Optimize timetable using hill climbing
    optimized_timetable, optimized_schedule = hill_climbing(timetable, schedule)

    print("\nOptimized Timetable (Slot-based):")
    print_slot_based_timetable(optimized_timetable, courses_details)
else:
    print("Failed to generate an initial timetable.")