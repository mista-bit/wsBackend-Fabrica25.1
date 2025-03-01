from django.shortcuts import render, redirect
from .services import convert_currency, get_exchange_rate
from .forms import CurrencyExchangeForm
from .models import Valores_Convertidos

# Os nomes das moedas foram escritos pela IA DeepSeek e pode conter erros
currency_names = {
    "AED": "Dirham dos Emirados Árabes Unidos",
    "AFN": "Afegane Afegão",
    "ALL": "Lek Albanês",
    "AMD": "Dram Armênio",
    "ANG": "Florim das Antilhas Holandesas",
    "AOA": "Kwanza Angolano",
    "ARS": "Peso Argentino",
    "AUD": "Dólar Australiano",
    "AWG": "Florim de Aruba",
    "AZN": "Manat Azeri",
    "BAM": "Marco Conversível da Bósnia e Herzegovina",
    "BBD": "Dólar de Barbados",
    "BDT": "Taka Bangladeshi",
    "BGN": "Lev Búlgaro",
    "BHD": "Dinar Bareinita",
    "BIF": "Franco Burundinense",
    "BMD": "Dólar Bermudense",
    "BND": "Dólar de Brunei",
    "BOB": "Boliviano",
    "BRL": "Real Brasileiro",
    "BSD": "Dólar das Bahamas",
    "BTC": "Bitcoin",
    "BTN": "Ngultrum Butanês",
    "BWP": "Pula de Botswana",
    "BYN": "Rublo Bielorrusso",
    "BYR": "Rublo Bielorrusso (antigo)",
    "BZD": "Dólar de Belize",
    "CAD": "Dólar Canadense",
    "CDF": "Franco Congolês",
    "CHF": "Franco Suíço",
    "CLF": "Unidade de Fomento Chilena",
    "CLP": "Peso Chileno",
    "CNY": "Yuan Chinês",
    "CNH": "Yuan Chinês Offshore",
    "COP": "Peso Colombiano",
    "CRC": "Colón Costarriquenho",
    "CUC": "Peso Cubano Conversível",
    "CUP": "Peso Cubano",
    "CVE": "Escudo Cabo-verdiano",
    "CZK": "Coroa Checa",
    "DJF": "Franco Djiboutiano",
    "DKK": "Coroa Dinamarquesa",
    "DOP": "Peso Dominicano",
    "DZD": "Dinar Argelino",
    "EGP": "Libra Egípcia",
    "ERN": "Nakfa Eritreia",
    "ETB": "Birr Etíope",
    "EUR": "Euro",
    "FJD": "Dólar de Fiji",
    "FKP": "Libra das Ilhas Falkland",
    "GBP": "Libra Esterlina",
    "GEL": "Lari Georgiano",
    "GGP": "Libra de Guernsey",
    "GHS": "Cedi Ganês",
    "GIP": "Libra de Gibraltar",
    "GMD": "Dalasi Gambiano",
    "GNF": "Franco Guineense",
    "GTQ": "Quetzal Guatemalteco",
    "GYD": "Dólar da Guiana",
    "HKD": "Dólar de Hong Kong",
    "HNL": "Lempira Hondurenha",
    "HRK": "Kuna Croata",
    "HTG": "Gourde Haitiano",
    "HUF": "Forint Húngaro",
    "IDR": "Rupia Indonésia",
    "ILS": "Novo Shekel Israelense",
    "IMP": "Libra de Man",
    "INR": "Rupia Indiana",
    "IQD": "Dinar Iraquiano",
    "IRR": "Rial Iraniano",
    "ISK": "Coroa Islandesa",
    "JEP": "Libra de Jersey",
    "JMD": "Dólar Jamaicano",
    "JOD": "Dinar Jordaniano",
    "JPY": "Iene Japonês",
    "KES": "Xelim Queniano",
    "KGS": "Som Quirguiz",
    "KHR": "Riel Cambojano",
    "KMF": "Franco Comorense",
    "KPW": "Won Norte-coreano",
    "KRW": "Won Sul-coreano",
    "KWD": "Dinar Kuwaitiano",
    "KYD": "Dólar das Ilhas Cayman",
    "KZT": "Tenge Cazaque",
    "LAK": "Kip Laosiano",
    "LBP": "Libra Libanesa",
    "LKR": "Rupia do Sri Lanka",
    "LRD": "Dólar Liberiano",
    "LSL": "Loti do Lesoto",
    "LTL": "Litas Lituano",
    "LVL": "Lats Letão",
    "LYD": "Dinar Líbio",
    "MAD": "Dirham Marroquino",
    "MDL": "Leu Moldavo",
    "MGA": "Ariary Malgaxe",
    "MKD": "Dinar Macedônio",
    "MMK": "Kyat de Mianmar",
    "MNT": "Tugrik Mongol",
    "MOP": "Pataca de Macau",
    "MRU": "Ouguiya Mauritana",
    "MUR": "Rupia Mauriciana",
    "MVR": "Rufiyaa Maldiva",
    "MWK": "Kwacha Malauiana",
    "MXN": "Peso Mexicano",
    "MYR": "Ringgit Malaio",
    "MZN": "Metical Moçambicano",
    "NAD": "Dólar Namibiano",
    "NGN": "Naira Nigeriana",
    "NIO": "Córdoba Nicaraguense",
    "NOK": "Coroa Norueguesa",
    "NPR": "Rupia Nepalesa",
    "NZD": "Dólar Neozelandês",
    "OMR": "Rial Omanense",
    "PAB": "Balboa Panamenho",
    "PEN": "Sol Peruano",
    "PGK": "Kina Papua-Nova Guiné",
    "PHP": "Peso Filipino",
    "PKR": "Rupia Paquistanesa",
    "PLN": "Zloty Polonês",
    "PYG": "Guarani Paraguaio",
    "QAR": "Rial Catariano",
    "RON": "Leu Romeno",
    "RSD": "Dinar Sérvio",
    "RUB": "Rublo Russo",
    "RWF": "Franco Ruandês",
    "SAR": "Riyal Saudita",
    "SBD": "Dólar das Ilhas Salomão",
    "SCR": "Rupia das Seychelles",
    "SDG": "Libra Sudanesa",
    "SEK": "Coroa Sueca",
    "SGD": "Dólar de Singapura",
    "SHP": "Libra de Santa Helena",
    "SLE": "Leone de Serra Leoa",
    "SLL": "Leone de Serra Leoa (antigo)",
    "SOS": "Xelim Somaliano",
    "SRD": "Dólar Surinamês",
    "STD": "Dobra de São Tomé e Príncipe",
    "SVC": "Colón Salvadorenho",
    "SYP": "Libra Síria",
    "SZL": "Lilangeni Suazi",
    "THB": "Baht Tailandês",
    "TJS": "Somoni Tajique",
    "TMT": "Manat Turcomeno",
    "TND": "Dinar Tunisiano",
    "TOP": "Paʻanga Tonganesa",
    "TRY": "Lira Turca",
    "TTD": "Dólar de Trinidad e Tobago",
    "TWD": "Dólar Taiuanês",
    "TZS": "Xelim Tanzaniano",
    "UAH": "Hryvnia Ucraniano",
    "UGX": "Xelim Ugandês",
    "USD": "Dólar Americano",
    "UYU": "Peso Uruguaio",
    "UZS": "Som Uzbeque",
    "VES": "Bolívar Venezuelano",
    "VND": "Dong Vietnamita",
    "VUV": "Vatu de Vanuatu",
    "WST": "Tala Samoano",
    "XAF": "Franco CFA Central",
    "XAG": "Prata (onça troy)",
    "XAU": "Ouro (onça troy)",
    "XCD": "Dólar do Caribe Oriental",
    "XDR": "Direitos Especiais de Saque",
    "XOF": "Franco CFA Ocidental",
    "XPF": "Franco CFP",
    "YER": "Rial Iemenita",
    "ZAR": "Rand Sul-africano",
    "ZMK": "Kwacha Zambiano (antigo)",
    "ZMW": "Kwacha Zambiano",
    "ZWL": "Dólar Zimbabuense",
}

def converter_moeda(request):
    valor_convertido = None
    moeda_base = None
    moeda_destino = None
    historico = Valores_Convertidos.objects.all().order_by('-data') 

    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        moeda_base = request.POST.get('moeda_base') 
        moeda_destino = request.POST.get('moeda_destino') 

        try:
            valor = float(valor)
            if valor <= 0:
                raise ValueError("O valor deve ser positivo.")
        except (ValueError, TypeError):
            return render(
                request,
                'index.html',
                {"error": "O valor inserido não é válido. Tente novamente.", "historico": historico, "currency_names": currency_names}
            )

        valor_convertido = convert_currency(valor, moeda_base, moeda_destino)

        Valores_Convertidos.objects.create(
            nome=nome,
            moeda_de_origem=moeda_base,
            moeda_destino=moeda_destino,
            valor_de_origem=valor,
            valor_destino=valor_convertido
        )

        return redirect('converter_moeda') 

    return render(
        request,
        'index.html',
        {
            "valor_convertido": valor_convertido,
            "moeda_base": moeda_base, 
            "moeda_destino": moeda_destino, 
            "currency_names": currency_names,
            "historico": historico,
        }
    )