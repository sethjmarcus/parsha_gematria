from hebrew import Hebrew
from hebrew import GematriaTypes
parshas_trope = [Hebrew("בְּרֵאשִׁ֖ית"),Hebrew("נֹ֔חַ"),Hebrew("לֶךְ לְךָ֛"),Hebrew("וַיֵּרָ֤א"),Hebrew("חַיֵּ֣י שָׂרָ֔ה"),Hebrew("תּוֹלְדֹ֥ת"),Hebrew("וַיֵּצֵ֥א"),Hebrew("וַיִּשְׁלַ֨ח"),Hebrew("וַיֵּ֣שֶׁב"), Hebrew("מִקֵּ֖ץ"),Hebrew("וַיִּגַּ֨שׁ"),Hebrew("וַיְחִ֤י"),Hebrew("שְׁמוֹת֙"),Hebrew("וָאֵרָ֗א"),Hebrew("בֹּ֖א"),Hebrew("בְּשַׁלַּ֣ח"),Hebrew("יִתְר֨וֹ"),Hebrew("מִּשְׁפָּטִ֔ים"),Hebrew("תְּרוּמָ֑ה"),Hebrew("תְּצַוֶּ֣ה"),Hebrew("כִּ֣י תִשָּׂ֞א"),Hebrew("וַיַּקְהֵ֣ל"),Hebrew("פְקוּדֵ֤י"),Hebrew("וַיִּקְרָ֖א"),Hebrew("צַ֤ו"),Hebrew("הַשְּׁמִינִ֔י"),Hebrew("תַזְרִ֔יעַ"),Hebrew("הַמְּצֹרָ֔ע"),Hebrew("אַחֲרֵ֣י מ֔וֹת"),Hebrew("קְדֹשִׁ֣ים"),Hebrew("אֱמֹ֥ר"),Hebrew("בְּהַ֥ר"),Hebrew("בְּחֻקֹּתַ֖י"),Hebrew("בְּמִדְבַּ֥ר"),Hebrew("נָשֹׂ֗א"),Hebrew("בְּהַעֲלֹֽתְךָ֙"),Hebrew("שְׁלַח"),Hebrew("קֹ֔רַח"),Hebrew("חֻקַּ֣ת"),Hebrew("בָּלָ֖ק"),Hebrew("פִּֽינְחָ֨ס"),Hebrew("מַּטּ֔וֹת"),Hebrew("מַסְעֵ֣י"),Hebrew("דְּבָרִ֗ים"),Hebrew("וָאֶתְחַנַּ֖ן"),Hebrew("עֵ֣קֶב"),Hebrew("רְאֵ֗ה"),Hebrew("שֹׁפְטִ֣ים"),Hebrew("כִּֽי־תֵצֵ֥א"),Hebrew("כִּֽי תָב֣וֹא"),Hebrew("נִצָּבִ֤ים"),Hebrew("וַיֵּ֖לֶךְ"),Hebrew("הַאֲזִ֥ינוּ"),Hebrew("וְזֹ֣את הַבְּרָכָ֗ה")]
parshas_no_trope = [Hebrew("בראשית"),Hebrew("נח"),Hebrew("לך לך"),Hebrew("וירא"),Hebrew("חיי שרה"),Hebrew("תולדת"),Hebrew("ויצא"),Hebrew("וישלח"),Hebrew("וישב"), Hebrew("מקץ"),Hebrew("ויגש"),Hebrew("ויחי"),Hebrew("שמות"),Hebrew("וארא"),Hebrew("בא"),Hebrew("בשלח"),Hebrew("יתרו"),Hebrew("משפטים"),Hebrew("תרומה"),Hebrew("תצוה"),Hebrew("כי תשא"),Hebrew("ויהקל"),Hebrew("פקודי"),Hebrew("ויקרא"),Hebrew("צו"),Hebrew("שמיני"),Hebrew("תזריע"),Hebrew("מצרע"),Hebrew("מות אחרי"),Hebrew("קדשים"),Hebrew("אמר"),Hebrew("בהר"),Hebrew("בחקתי"),Hebrew("במדבר"),Hebrew("נשא"),Hebrew("בהעלתך"),Hebrew("שלח"),Hebrew("קרח"),Hebrew("חקת"),Hebrew("בלק"),Hebrew("פינחס"),Hebrew("מטות"),Hebrew("מסעי"),Hebrew("דברים"),Hebrew("ואתחנן"),Hebrew("עקב"),Hebrew("ראה"),Hebrew("שפטים"),Hebrew("כי תצא"),Hebrew("תבוא כי"),Hebrew("נצבים"),Hebrew("וילך"),Hebrew("האזינו"),Hebrew("וזאת הברכה")]

map = {}
for gem in GematriaTypes:
    map[gem] = {}
    for par in parshas_trope:
        gem_value = par.gematria(gem)
        if gem_value not in map[gem]:
            map[gem][gem_value] = []
        map[gem][gem_value].append(par)

for gem in map:
    print(gem)
    obj = map[gem]
    for k in obj:
        if len(obj[k]) >= 2:
            print(obj[k], k, "\t")
    print()