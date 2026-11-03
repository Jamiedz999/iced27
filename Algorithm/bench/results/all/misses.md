# Queries not found in the top 5 (levenshtein): 6109 of 16791

Read each row and ask: is the gold alignment right? Is the top-1 window a genuinely similar passage (a repeated formula, say)? Or is it noise?

Showing the first 300; all are in `per_query.csv`.

| Segment | Q | Query (medieval) | Gold (modern) | Gold score / rank | Top-1 segment | Top-1 score | Top-1 window |
|---|---:|---|---|---|---|---:|---|
| AidedCheltC_0_3_8 | 2 | Atrulla Celtchar | Do theith Cealtchar | 0.4841 / 14 (tied 9) | AidedCheltC_0_5_1 | 0.4127 | ar cealtchar |
| AidedCheltC_0_6_1 | 2 | Dogníther ón | Do ghníthear san, | 0.5556 / 6 | AidedCheltC_0_12_1 | 0.4444 | sinn ón |
| abbot_0_1_1 | 8 | Aroile hóclach ro baei a n-abduine Druimenaigh | Bhí ógfhear áirithe ina ab ar Dhroimeanach | 0.6723 / 63 | abbot_0_4_5 | 0.5059 | dhubhach dheorach dhobrónach a bhí an duine eile |
| abbot_0_1_2 | 11 | tríallthar lais fled mórcaín móradh do dénam do fritheólad na Cásc. | agus bheartaigh sé ar fhleá mhór thaitneamhach a eagrú chun an Cháisc a cheiliúradh. | 0.6349 / 8 (tied 1) | abbot_0_7_4 | 0.5844 | na cásca agus chuaigh sise in éineacht leis an airchinneach go dtí |
| abbot_0_2_1 | 5 | Íar n-ullmadhadh na fledhi, | Tar éis dó an fhleá a ullmhú, | 0.6048 / 17 | abbot_0_7_3 | 0.5400 | le cuireadh ar ócáid na |
| abbot_0_3_1 | 6 | Et íar muscladh dó asa collud, | Agus nuair a dhúisigh sé as a chodladh | 0.7014 / 34 (tied 1) | abbot_0_8_4 | 0.5625 | chlann a roinnt ar a dó |
| abbot_0_3_7 | 7 | ocus an úair tuc lám tara oigedh, | Nuair a chuir a lámh lena aghaidh | 0.5905 / 10 | abbot_0_2_10 | 0.4871 | ina láimh agus ar shroicheadh an tulaigh |
| abbot_0_4_7 | 6 | Uair cia dom-tigh de dhechar, | Mar cibé anachain a rinneadh orm, | 0.6736 / 28 | abbot_0_5_3 | 0.5369 | taobh thiar de dhroimeanach ansin bhuail |
| abbot_0_4_14 | 10 | ocus dom-rad a n-héccruth ocus a n-aindricht. | is a chuir as mo chló agus as mo riocht mé. | 0.6361 / 49 | abbot_0_8_4 | 0.5361 | ná an chlann a roinnt ar a dó agus an seachtú |
| abbot_0_4_15 | 10 | Acht chena, cía dom-rad Dia a n-aitherruch hécaisc, | Ach cé gur chuir Dia as mo chruth ceart mé, | 0.5844 / 18 | abbot_0_1_2 | 0.5477 | thaitneamhach a eagrú chun an cháisc a cheiliúradh tar éis dó |
| abbot_0_4_16 | 8 | do-beirim fom’ bréithir a bhfhíadhnaisi an Dúilim | dearbhaím i bhfianaise an Chruthaitheora | 0.6701 / 69 | abbot_0_7_7 | 0.5133 | rompu go dtí an chill nuair a dhúisigh |
| abbot_0_4_24 | 9 | ocus is ed ro ráidh, ac éirghe don cnuc: | agus is é a dúirt, agus é ag imeacht ón gcnoc: | 0.5897 / 8 | abbot_0_8_6 | 0.5278 | don airchinneach agus is amhlaidh sin a scaradar lena chéile |
| abbot_0_5_6 | 9 | ocus ro gabh fora guidhe ocus nír gabh úaithe | Níor stad sé de bheith ag impí uirthi | 0.7407 / 89 | abbot_0_4_17 | 0.6071 | duine agus nach ndearna mé feall ar éinne agus nár |
| abbot_0_5_7 | 7 | co ndechaid ina gnáis ocus ina caomhthach | go dtí gur ghlac sise leis mar leannán agus mar chompánach grámhar | 0.7117 / 65 | abbot_0_7_12 | 0.4988 | ghoil go deorach agus ina dhiaidh sin |
| abbot_0_7_1 | 6 | Tic íar sin techta cusan oirchindech | Tamall ina dhiaidh sin, tháinig teachtaire go dtí an airchinneach | 0.5791 / 8 | abbot_0_7_14 | 0.4977 | sin bhíothas tar éis an proinnteach |
| abbot_0_7_6 | 11 | ocus do-fuit a collud fuirri-si fo cétóir isin cnuc | agus thit codladh uirthi láithreach ar an gcnoc | 0.5965 / 13 | abbot_0_7_12 | 0.5519 | go deorach agus ina dhiaidh sin chuaigh sé go dtí a chéad |
| abbot_0_7_8 | 7 | ocus íar mussclad don ingin asa collud, | Nuair a dhúisigh an bhean óg as a codladh, | 0.6648 / 27 | abbot_0_8_5 | 0.5536 | ar altramas don airchinneach agus is amhlaidh |
| abbot_0_7_13 | 16 | ocus as-pert a bhen fris íarum: “Is rófhada a-taí a n-hécmais do thighe.” | agus ansin dúirt a bhean leis: “Bhí tú rófhada amuigh.” | 0.4967 / 7 | abbot_0_7_8 | 0.4497 | a mhuintir rompu go dtí an chill nuair a dhúisigh an bhean óg as a codladh is |
| abbot_0_7_14 | 11 | Is ann-sin ro baí an tegh n-óla arna oiregar | Faoin am sin bhíothas tar éis an proinnteach a fháil réidh | 0.5422 / 13 | abbot_0_5_3 | 0.4528 | is é sin le rá cill a bhí ar an taobh thiar |
| acSen_1_7_6 | 4 | ocus iat ina súidhi. | agus iadsan ina suí. | 0.5000 / 7 (tied 1) | acSen_4_2_9 | 0.4345 | ina deichiú bliain agus |
| acSen_2_1_1 | 8 | Ocus do bhátur annsin co táinic maden arnamárach, | Do bhíodar ann gur tháinig mochshoilse arna mhárach, ag idirmholadh an Dúileamhan. | 0.5481 / 12 | acSen_3_5_1 | 0.4940 | chaoil tháinig an iníon ansin agus do shín |
| acSen_3_1_6 | 5 | ‘Cret do iarais?’ ar Finn. | ‘Céard d’iarrais ann?’ arsa Fionn. | 0.4686 / 22 | acSen_4_2_5 | 0.3733 | fionn agus do bhí ar |
| acSen_3_1_11 | 7 | ‘Adersa sin rit,’ ar Finn — Fr. 12a | ‘Inseoidh mé duit faoi sin,’ arsa Fionn, | 0.5201 / 8 | acSen_3_1_8 | 0.4082 | a ábhar sin arsa fionn ar bhíthin |
| acSen_3_2_71 | 4 | Lebaidh luchair na line | Leaba luchair go gcaoine | 0.5357 / 34 (tied 1) | acSen_4_7_15 | 0.4196 | gonadh ard na tine |
| acSen_3_2_128 | 3 | éirghit isin frithdhaileam, | éiríd insa fhriotháileamh; | 0.5833 / 7 | acSen_2_1_2 | 0.5326 | éirigh padraig ansin |
| acSen_3_4_10 | 4 | .i. a badadh Caeil, | .i. Caol do bhá iar líonadh an láin mhara thairis; | 0.5167 / 45 | acSen_3_4_8 | 0.3083 | caol i a fear |
| acSen_4_2_9 | 5 | a cind a deich mbliadna, | agus é ina deichiú bliain, | 0.5821 / 88 | acSen_4_2_5 | 0.3283 | ceann a dheich mbliana agus |
| acSen_4_3_5 | 7 | Ocus do fiarfaig iarsin cuich in macaemh? | agus d’fhiafraigh iar sin cé an macaomh. | 0.5180 / 18 | acSen_3_6_3 | 0.4405 | chumha agus do adhlacadh iad araon in |
| acSen_4_9_7 | 5 | do gaet Aillén mac Midhna | goineadh Oilleán mac Mhíona | 0.4357 / 6 | acSen_4_8_1 | 0.3607 | do rathaigh oilleán mac mhíona |
| aidedBres_0_1_8 | 5 | ocus ní thuc in chaillech, | ach do dhiúltaigh an chailleach. | 0.6500 / 17 | aidedBres_0_2_4 | 0.4944 | ina cill agus dul in |
| aidedBres_0_1_11 | 6 | Intan rob aine doibh ic ol, | An uair is somheanmnaí a bhíodar ag ól | 0.6860 / 15 | aidedBres_0_2_6 | 0.5897 | gníomh do rinne tú ina dhiaidh sin |
| aidedBres_0_1_13 | 5 | do chasait Bresail cusin righ, | Do ghearán sí Breasal leis an rí | 0.5371 / 9 | aidedBres_0_1_6 | 0.3848 | rialta sin do chuaigh breasal |
| aidedBres_0_1_14 | 4 | ocus a heighmhe eisdi. | agus d’éigh sí. | 0.6062 / 12 (tied 2) | aidedBres_0_1_6 | 0.5194 | a cheannach agus do |
| aidedBres_0_4_1 | 7 | O rancatar iarum is ed fuaratar Becan | Nuair a shroiseadar an áit a raibh Beagán, is amhlaidh a bhí sé rompu | 0.6516 / 13 | aidedBres_0_3_1 | 0.6058 | maraítear breasal is ansin dúirt diarmaid le colum |
| aidedBres_0_4_4 | 4 | ocus ic irnaigthi simul. | agus é ag urnaí san am céanna. | 0.7194 / 11 (tied 1) | aidedBres_0_2_4 | 0.5667 | agus dul in aghaidh |
| aidedCheitM_0_5_9 | 3 | ocus an anr- | agus … a n-araí, | 0.5556 / 32 (tied 10) | aidedCheitM_0_9_2 | 0.3889 | agus fágann an |
| aidedCheitM_0_6_3 | 5 | “ar ná romaigset Connachta cetus.” | “...” | never ranked | aidedCheitM_0_3_1 | 0.5089 | so ar conall agus ní |
| aidedChel_0_3_8 | 2 | Atrulla Celtchar | Do theith Cealtchar | 0.4841 / 14 (tied 9) | aidedChel_0_5_1 | 0.4127 | ar cealtchar |
| aidedChel_0_6_1 | 2 | Dogníther ón | Do ghníthear san, | 0.5556 / 6 | aidedChel_0_12_1 | 0.4444 | sinn ón |
| aidedChonch_0_1_5 | 6 | co ro-acilliur ócu na comram.” | le go labhróinn leis na laochra atá ag iomaíocht.” | 0.6422 / 9 | aidedChonch_0_7_1 | 0.5518 | ard na gcon ach tiomáineadh ulaidh |
| aidedChonch_0_2_3 | 7 | écht fón innas-sa ar galaib óinfhir, | éacht den sort seo i gcomhrac aonair, | 0.6380 / 52 | aidedChonch_0_5_3 | 0.4735 | suas leis sa tóir air tháinig connachta ón |
| aidedChonch_0_4_1 | 9 | Intan bátar na ónmite ’co cluchiu do inchind Meisgegra, | Agus na hóinmhidí ag imirt le hinchinn Mheis Gheára, | 0.6255 / 18 | aidedChonch_0_8_1 | 0.5709 | go céile tar éis don rí imeacht briseadh ar na |
| aidedChonch_0_4_7 | 5 | nobíd do Chonnachtaib fri Ulto | a bhíodh ag Connachta le hUlaidh, | 0.7243 / 23 | aidedChonch_0_13_12 | 0.6433 | chonchúir go hifreann go dtí |
| aidedChonch_0_4_9 | 6 | dús in tetarthad écht n-amra | féachaint an rithfeadh leis éacht cáiliúil a dhéanamh | 0.6250 / 16 (tied 2) | aidedChonch_0_2_2 | 0.5730 | na laochra atá i gcomórtas éacht |
| aidedChonch_0_4_10 | 5 | d’ Ultaib do marbad di. | agus Ultach a mhárú léi. | 0.7667 / 63 (tied 4) | aidedChonch_0_7_4 | 0.5200 | uladh d aon duine a |
| aidedChonch_0_5_1 | 8 | Fecht and didiu dolluid-seom intí Cet sair | Ghabh Cead soir uair | 0.7205 / 95 (tied 1) | aidedChonch_0_3_4 | 0.5997 | céanna an phéist ba dheacra in éirinn mar seo |
| aidedChonch_0_5_3 | 7 | Donarraid i n-íarmóracht Ulaid ina diaid. | Tháinig na hUlaidh suas leis sa tóir air. | 0.6593 / 58 | aidedChonch_0_1_12 | 0.4844 | in iomarbhá nó i gcomórtais thugtaí chucu iad |
| aidedChonch_0_5_14 | 6 | etir erriud ocus áne ocus écosc, | idir fheisteas agus ghlóir agus dhealramh, | 0.6944 / 14 (tied 1) | aidedChonch_0_5_10 | 0.6194 | agus chló agus éide idir mhéid |
| aidedChonch_0_5_17 | 5 | Nírbo lochtach tra intí Conchobur. | Ní raibh locht, más ea, ar Chonchúr. | 0.6572 / 9 (tied 1) | aidedChonch_0_2_5 | 0.6267 | fíor sin arsa conchúr cuireadh |
| aidedChonch_0_5_20 | 10 | Luid íarum for leth a óinur dia déscin dona mnáib. | Chuaigh sé i leataoibh ina aonar ansin le go bhfeicfeadh na mná é. | 0.5899 / 16 | aidedChonch_0_9_1 | 0.5321 | briseadh ar na hulaidh ansin tugadh a lia i finín go |
| aidedChonch_0_6_2 | 6 | Nosindlethar Cet inchind Mesgegra isin tábaill | Chuir sé inchinn Mheis Gheára i bhfearas ina chrann tabhaill | 0.6571 / 8 | aidedChonch_0_2_5 | 0.5694 | sin arsa conchúr cuireadh an inchinn |
| aidedChonch_0_6_5 | 9 | ocus co torchairseom isa cend, co tarla fri lár. | agus gur thit sé i ndiaidh a chinn ar lár ar an talamh. | 0.6389 / 16 (tied 2) | aidedChonch_0_13_8 | 0.5868 | cheann agus go bhfuair conchúr bás ar an toirt is |
| aidedChonch_0_6_9 | 7 | Atá a lige and baile i torchair | Tá a uaigh ansiúd mar ar thit sé, | 0.4976 / 12 | aidedChonch_0_6_5 | 0.4592 | i ndiaidh a chinn ar lár ar an |
| aidedChonch_0_7_6 | 4 | Dobeir-side lomain imme | Chuir seisean téad ina thimpeall | 0.7054 / 14 | aidedChonch_0_12_4 | 0.6667 | morann an fear eile |
| aidedChonch_0_8_2 | 5 | Co ráimid for Ulto íarsin. | Briseadh ar na hUlaidh ansin. | 0.7095 / 18 (tied 1) | aidedChonch_0_5_20 | 0.6003 | aonar ansin le go bhfeicfeadh |
| aidedChonch_0_9_2 | 8 | Iss éside nofhinnad don díaid nothéiged don tig | Eisean a d’fhionnfadh ón deatach a thagadh ón teach | 0.7278 / 64 | aidedChonch_0_8_1 | 0.6194 | ar siúl ón tráth go céile tar éis don |
| aidedChonch_0_9_3 | 7 | in lín nobíd i ngalur ’sin tig | an líon duine a bhíodh easlán ann, | 0.6758 / 49 | aidedChonch_0_6_5 | 0.5068 | ina cheann agus gur thit sé i ndiaidh |
| aidedChonch_0_9_7 | 4 | Mani tucthar ass immorro, | Mura dtógfaí as í, áfach, | 0.6905 / 33 (tied 1) | aidedChonch_0_7_3 | 0.5565 | bhaoth tugtar mise as |
| aidedChonch_0_9_8 | 2 | not-ícfaind | dhéanfainn thú a leigheas | 0.8000 / 102 (tied 1) | aidedChonch_0_7_9 | 0.6071 | an nath |
| aidedChonch_0_10_1 | 5 | Ro-íccad íarum a chend | Leigheasadh a cheann ansin, | 0.5467 / 18 (tied 2) | aidedChonch_0_13_7 | 0.4467 | as a cheann agus go |
| aidedChonch_0_10_5 | 11 | co mbeth i fomtin.i. ar ná tísad a fherg dó | a bheith ar a aire nach dtiocfadh fearg air, | 0.5667 / 25 | aidedChonch_0_5_7 | 0.4561 | chath is ansin a d impigh mná chonnacht ar chonchúr teacht i |
| aidedChonch_0_10_6 | 5 | ocus ná digsed for ech | agus gan dul ar each, | 0.6500 / 7 (tied 3) | aidedChonch_0_11_6 | 0.6200 | na dúile agus chrith neamh |
| aidedChonch_0_10_7 | 4 | ocus ná etraiged mnái | agus gan luí le bean, | 0.8125 / 112 (tied 5) | aidedChonch_0_5_17 | 0.5563 | ní raibh locht más |
| aidedChonch_0_10_8 | 6 | ocus ná rocaithed biad co anfeta | agus gan bia a chaitheamh le hampla, | 0.6972 / 32 | aidedChonch_0_9_10 | 0.6204 | is fusa linn an aithis ná |
| aidedChonch_0_10_9 | 3 | ocus ná rethed. | agus gan rith. | 0.6667 / 16 (tied 3) | aidedChonch_0_9_10 | 0.5556 | an aithis ná |
| aidedChonch_0_11_2 | 3 | ocus nírbo engnamaid, | agus gan é inghníomha | 0.7593 / 62 (tied 21) | aidedChonch_0_1_12 | 0.5889 | díobh agus nuair |
| aidedChonch_0_11_4 | 8 | .i. naco cúala Críst do chrochad do Iudaidib. | nó gur chuala sé gur chéas na Giúdaigh Críost ar chrois. | 0.6406 / 32 | aidedChonch_0_11_8 | 0.4896 | i íosa críost mac dé a chéasadh ar chrois |
| aidedChonch_0_11_7 | 6 | la mét in gníma darónad and | le huafás an ghnímh a rinneadh ansin | 0.5694 / 6 | aidedChonch_0_3_4 | 0.5119 | céanna an phéist ba dheacra in |
| aidedChonch_0_11_11 | 7 | “Is fir ón ém,” ar in drúi. | “Is fíor dhuit,” arsan draoi. | 0.5000 / 7 | aidedChonch_0_7_10 | 0.3929 | ar ulaidh is é sin an rí ar |
| aidedChonch_0_11_14 | 7 | “i n-óenaidchi rogein ocus rogenis-siu | “rugadh é an oíche chéanna leat féin | 0.6129 / 12 | aidedChonch_0_1_6 | 0.5777 | leis na hulaidh an uair sin a n |
| aidedChonch_0_12_2 | 5 | Ocus issé sin indara fer | Ba dhuine é den bheirt | 0.7262 / 70 (tied 4) | aidedChonch_0_2_5 | 0.4762 | is fíor sin arsa conchúr |
| aidedChonch_0_13_6 | 7 | Is iarsin attraacht ocus rosgobh forsin deargail | Is ansin a d’éirigh sé agus a thug faoin gcoill daraí | 0.5992 / 7 | aidedChonch_0_5_6 | 0.5638 | eatarthu chuaigh conchúr féin sa chath is ansin |
| aidedConr_0_1_2 | 2 | Ní hansa. | Ní deacair san. | 0.4286 / 9 (tied 1) | aidedConr_0_5_23 | 0.3000 | ní haon |
| aidedConr_0_1_3 | 4 | Im Bláthnait ingin Mind | Mar gheall ar Bhláthnaid, iníon Mheann, | 0.5667 / 6 | aidedConr_0_15_10 | 0.5153 | náire mo léan bláthnaid iníon |
| aidedConr_0_1_4 | 5 | tucad a forbais fer Failgi | a hardaíodh chun siúil tar éis léigear na bhFear Fálga, | 0.5629 / 26 (tied 2) | aidedConr_0_6_13 | 0.4262 | is faoi sin a canadh fear |
| aidedConr_0_1_10 | 4 | Bo hé al-lóeg. | Gamhain na dtrí mbó a thugtaí ar an gcoire seo, | 0.7560 / 189 (tied 4) | aidedConr_0_4_11 | 0.5625 | do labhair sé leis an |
| aidedConr_0_1_11 | 6 | Tricha aigi a lucht in choiri | spás ann do thríocha damh. | 0.6736 / 217 | aidedConr_0_12_106 | 0.3952 | deich bhfathach cnoic nuair a chuaigh lucht |
| aidedConr_0_1_13 | 6 | Is de asbert Cúchulaind isin tSíabarcharpat: | Mar seo a thagair Cú Chulainn dó sa Siabharcharbad: | 0.5996 / 43 | aidedConr_0_4_23 | 0.4857 | sin is é comhartha do sochraíodh eatarthu |
| aidedConr_0_1_17 | 4 | tricha aigi ina chróis, | Tríocha damh ina bholg | 0.5089 / 10 (tied 1) | aidedConr_0_9_15 | 0.4554 | ina charbad thiomáin na heacha |
| aidedConr_0_1_18 | 5 | ised sin fo lucht dó. | choimeádfadh sé gan stró. | 0.7933 / 270 (tied 1) | aidedConr_0_6_12 | 0.4800 | laoch díobh leis is faoi sin |
| aidedConr_0_1_20 | 4 | Tathaigtis in coiri sin, | Ba thaithneamhach mar dhúshlán é: | 0.6458 / 100 | aidedConr_0_14_1 | 0.3063 | sin bhuail in aghaidh carraige |
| aidedConr_0_1_21 | 4 | ba mellach in bág, | bhailídís ina thimpeall | 0.7188 / 228 (tied 1) | aidedConr_0_15_13 | 0.4167 | d éag sa tsléacht in |
| aidedConr_0_1_22 | 4 | ni théigdis úad atherrach | is ní imídís | 0.7153 / 177 | aidedConr_0_5_13 | 0.5104 | na cathrach más daracha iad |
| aidedConr_0_1_26 | 4 | robo maith in fríth. | bhí ann — ba mhaith an ciste. | 0.5542 / 9 | aidedConr_0_12_119 | 0.3786 | in aghaidh bíobhaí ní maith |
| aidedConr_0_1_27 | 5 | Dobert-sa in core sin | Mise d’ardaigh chun siúil an coire | 0.5981 / 53 (tied 1) | aidedConr_0_14_1 | 0.4583 | iar sin bhuail in aghaidh carraige |
| aidedConr_0_1_28 | 4 | la hingin ind ríg.” | i dteannta iníon an ruire.” | 0.7060 / 154 (tied 1) | aidedConr_0_4_13 | 0.5000 | í iníon iuchna rí na |
| aidedConr_0_2_2 | 2 | ocus nínaithgéntair | ach chuaigh díobh é a aithint. | 0.7232 / 49 | aidedConr_0_6_1 | 0.5357 | chathair agus |
| aidedConr_0_2_3 | 6 | .i. ‘fer broit lachtna’ asbertadar fris. | Thugadar ‘an fear sa chlócha ar dhath an uachtair’ air. | 0.6714 / 51 | aidedConr_0_4_9 | 0.5651 | i srúibh brain is é a tharla |
| aidedConr_0_2_5 | 5 | Cach cend doberthea asin dún, | De réir mar a thugtaí cloigne na marbh as an ndún | 0.5906 / 16 | aidedConr_0_2_1 | 0.4567 | dáire leosan ansin don léigear ach |
| aidedConr_0_2_6 | 7 | “Cía romarb in fer sin?” ar Conchobar. | d’fhiafraíodh Conchobhar: “Cé mharaigh an fear san?” | 0.4548 / 6 | aidedConr_0_4_22 | 0.4167 | féin ina aonar ina chathair ar an lá sin |
| aidedConr_0_3_1 | 7 | Intan didu rombatha ic roind na broiti | Nuair a bhí sé in am an chreach a roinnt, áfach, | 0.6167 / 44 | aidedConr_0_4_6 | 0.5204 | siad nó gur shroich srúibh brain in iarthar na |
| aidedConr_0_3_2 | 4 | ní rochutigsead in Coinrúi, | níor chuidíodar le Cú Raoi | 0.6369 / 69 (tied 6) | aidedConr_0_12_119 | 0.4226 | in aghaidh bíobhaí ní maith |
| aidedConr_0_3_3 | 5 | ar nirdamad íarum cert dó. | agus ní bhfuair sé a cheart ansin. | 0.6617 / 90 | aidedConr_0_10_7 | 0.4644 | cheart a thabhairt anois dó arsa |
| aidedConr_0_3_5 | 2 | corustimairc remi | Thiomáin roimis iad. | 0.6667 / 12 (tied 4) | aidedConr_0_1_1 | 0.6250 | raoi mac |
| aidedConr_0_3_7 | 7 | ocus co tarad in mnái ina lethuscaill | Bhuail an bhean fé cheann dá ascaillí. | 0.5910 / 38 | aidedConr_0_8_3 | 0.4865 | coirthe a bhfuil ina seasamh agus ina luí in |
| aidedConr_0_3_8 | 4 | ocus no lodadar úadaib | D’imíodar uathu | 0.7054 / 87 | aidedConr_0_6_8 | 0.5667 | theach air agus go ndeachadar |
| aidedConr_0_3_10 | 8 | ocus ní roacht neach do Ultaib comacallaim fair | Níor fhéad éinne d’fheara Uladh dul chun comhchainte leis | 0.6335 / 74 | aidedConr_0_1_1 | 0.5032 | uladh cú raoi mac dáire do chur chun báis ní |
| aidedConr_0_3_11 | 4 | acht Cúchulaind a óenur. | ach Cú Chulainn amháin. | 0.5458 / 43 (tied 1) | aidedConr_0_9_2 | 0.4125 | cú chulainn a cheann den |
| aidedConr_0_3_12 | 2 | Imsói friside | Ach d’iompaigh Cú Raoi air. | 0.7411 / 55 (tied 2) | aidedConr_0_11_8 | 0.5857 | is féidir |
| aidedConr_0_3_13 | 7 | contarad isin talmain conici a dá ascaill | Chuir tríd an dtalamh síos go dtína dhá ascaill é. | 0.4995 / 9 | aidedConr_0_11_7 | 0.4346 | an cháith dá uireasa éagmais chinniúnach a chailliúint is |
| aidedConr_0_3_14 | 7 | ocus co roberr máil fair cosin chloduib, | Bhearr an ghruaig dó leis an gclaíomh gur fhág maol é. | 0.7440 / 212 | aidedConr_0_3_12 | 0.5655 | chulainn amháin ach d iompaigh cú raoi air chuir |
| aidedConr_0_3_15 | 8 | ocus co rochomail cacc ina mbó inna chend, | Chuimil bualtach bó dá cheann. | 0.6424 / 65 | aidedConr_0_1_16 | 0.4872 | coire gamhain na dtrí mbó tríocha damh ina bholg choimeádfadh |
| aidedConr_0_4_2 | 10 | A mbúi-seom didu laa n-and for Bendaib Bairchi | Lá agus é ar bharra na mBeanna Boirche, áfach, | 0.6140 / 83 | aidedConr_0_9_1 | 0.5071 | ar dhá mhíle ach nuair a bhíodar á n imghoin um an |
| aidedConr_0_4_3 | 11 | co n-acai éill móir do énaib dubuib chuigi darsin fairrgi. | chonaic chuige thar an bhfarraige anall ealt mhór d’éin dhubha. | 0.5482 / 6 | aidedConr_0_14_12 | 0.5386 | an comhlann i gcomhar do bhláithnaid agus do fhearcheirtne cóir uaigh na beirte acu |
| aidedConr_0_4_7 | 8 | .i. a cend tall-som dond eón dub, | Ó ghob an fhiaigh dhuibh a mharaigh sé ansin | 0.5479 / 13 (tied 2) | aidedConr_0_11_2 | 0.4955 | chur dem chroí monuar mura mbeadh bean a theacht i |
| aidedConr_0_4_8 | 5 | is de dogairther Srub Broin. | a hainmníodh an áit.i. Srúibh Brain. | 0.5000 / 7 (tied 2) | aidedConr_0_4_17 | 0.4900 | sí comhairle do chú raoi is |
| aidedConr_0_4_9 | 6 | Ised dorala anniar do chathraig Conrái, | Is é a tharla gur thug aniar dó go cathair Chú Raoi é. | 0.5833 / 18 (tied 3) | aidedConr_0_5_10 | 0.4603 | do dhéanamh na cathrach más daracha iad |
| aidedConr_0_4_10 | 8 | conad and rofiter is é dorad mebal fair | Tuigeadh dó gurbh é siúd ba chúis lena náiriú. | 0.5598 / 33 | aidedConr_0_4_22 | 0.4608 | aonar ina chathair ar an lá sin is é comhartha |
| aidedConr_0_4_11 | 5 | ocus roacaill ’no in mnái, | Do labhair sé leis an bhean ansin, | 0.6333 / 30 (tied 3) | aidedConr_0_8_3 | 0.5333 | ina seasamh agus ina luí in |
| aidedConr_0_4_12 | 7 | ar rocharastair cid síu thuctha dar muir; | óir bhí grá aige di sular tugadh thar muir í. | 0.5602 / 25 | aidedConr_0_7_17 | 0.4830 | sé a dhún féin ar barr lasrach thar muir |
| aidedConr_0_4_14 | 8 | .i. fál mara i n-indsib mara nobítis. | . | never ranked | aidedConr_0_4_21 | 0.5330 | éirinn dob iad clanna deadhadh do ghluais i n aonlá |
| aidedConr_0_4_15 | 8 | Rodál-som fria si síar aridhisi aidchi Samna. | Bheartaíodar bualadh le chéile arís sa bhall céanna um Oíche Shamhna. | 0.6430 / 13 | aidedConr_0_5_14 | 0.5979 | iad siad san na clocha ar leith d ardaigh sé |
| aidedConr_0_4_18 | 9 | .i. ara ndénta daingen n-amra leis dia chathraig | is é sin, rampair amhra a thógaint dá dhún agus an caiseal a dhaingniú | 0.5948 / 58 | aidedConr_0_4_21 | 0.4854 | clanna deadhadh do ghluais i n aonlá do dhéanamh na cathrach |
| aidedConr_0_4_20 | 4 | Is í cland Dedad | Dob iad Clanna Deadhadh | 0.5938 / 33 | aidedConr_0_10_9 | 0.4583 | rí is dóichí gurb í |
| aidedConr_0_4_26 | 2 | Dogníther ón. | Rinneadh amhlaidh. | 0.8889 / 310 (tied 50) | aidedConr_0_11_8 | 0.2778 | ón aonfhear |
| aidedConr_0_5_3 | 3 | co rofhoilcther duit | “chun go nífear do cheann | 0.6944 / 54 (tied 11) | aidedConr_0_10_4 | 0.4833 | go maith dhuit |
| aidedConr_0_5_7 | 4 | iter chois ocus ech. | cuid acu de shiúl na gcos, a thuilleadh ar muin capall. | 0.6562 / 54 (tied 1) | aidedConr_0_12_21 | 0.5595 | soitheach deich gcupa de chlocha |
| aidedConr_0_5_13 | 5 | “Masdo daraig is lúath ráit, | “Más daracha iad, sin iad na crainn atá ag scinneadh go tapaidh. | 0.6324 / 42 | aidedConr_0_4_8 | 0.4433 | an áit i srúibh brain is |
| aidedConr_0_5_14 | 4 | is búaid masda licc.” | Más clocha iad, siad san na clocha ar leith.” | 0.6262 / 49 | aidedConr_0_4_9 | 0.5083 | srúibh brain is é a |
| aidedConr_0_5_17 | 6 | Fecaid-sem beous fora ngrinigud-som. | D’amharc go grinn orthu a thuilleadh. | 0.6731 / 13 | aidedConr_0_9_22 | 0.6172 | féna tonnta searbha go deo tháinig fearcheirtne |
| aidedConr_0_5_18 | 4 | “Cía sud?” or se. | “Cad san ansan?” d’fhiafraigh sé. | 0.7000 / 77 (tied 4) | aidedConr_0_1_13 | 0.5833 | ceoil iad mar seo a |
| aidedConr_0_5_22 | 4 | “Masa cheathra condat ceathra | “Más eallach iad, nó gur ar dhath an eallaigh atáid, | 0.6994 / 147 (tied 10) | aidedConr_0_5_2 | 0.5104 | na cathrach tar sa chathair |
| aidedConr_0_5_23 | 3 | niddat alma chóelbó. | ní haon tréad bó caola iad. | 0.6603 / 6 (tied 2) | aidedConr_0_5_6 | 0.6270 | chonaic slua na |
| aidedConr_0_5_24 | 5 | Atá fer beg beartair fæbro | Cím firín, lann ar iompar aige, | 0.7133 / 68 | aidedConr_0_15_15 | 0.5517 | brath a fir nuair atá féna |
| aidedConr_0_6_1 | 3 | Lasodain gaibthi inund | Leis sin, gabhann sé anonn sa chathair | 0.7000 / 38 | aidedConr_0_7_6 | 0.6127 | cholainne ina uaigh |
| aidedConr_0_6_2 | 7 | ocus foilcid in bean dó.i. foidlcad | agus tugann an bhean folcadh dhó. | 0.5405 / 6 | aidedConr_0_11_5 | 0.4476 | codladh an bháis tá i ndán dó feasta scaipfidh |
| aidedConr_0_6_3 | 9 | ocus rochumrigh a fholt dona cholbaib ocus dona tuireadhaib | Ceanglaíonn sí a dhlaoithe de phoist na leapan agus de na piléir. | 0.5864 / 15 | aidedConr_0_9_2 | 0.5374 | cú chulainn a cheann den fhear is do chuir an chathair |
| aidedConr_0_6_6 | 3 | Ní forchúala didu | Níor chuala sé aon ní, áfach, | 0.5926 / 15 (tied 5) | aidedConr_0_10_11 | 0.4722 | fearcheirtne file ní |
| aidedConr_0_6_9 | 5 | Atraig bacétóir do chomérgiu forro | Phreab ina sheasamh láithreach ina gcoinne | 0.7792 / 238 | aidedConr_0_15_2 | 0.5433 | ó shamhain go meán earraigh do |
| aidedConr_0_6_11 | 7 | Atrachta dóib in fer gaire robái istaig | Thug óinmhid a bhí istigh dóibh | 0.5765 / 13 | aidedConr_0_6_12 | 0.5262 | istigh dóibh gur thit tríocha laoch díobh leis is |
| aidedConr_0_6_13 | 3 | Is de rochét: | Is faoi sin a canadh: | 0.5833 / 39 (tied 1) | aidedConr_0_9_19 | 0.4333 | le háilleacht is |
| aidedConr_0_6_15 | 5 | “Cid fer gaire na flatha | Fear magaidh an tiarna | 0.5310 / 21 (tied 1) | aidedConr_0_15_3 | 0.4556 | dhealaigh na hultaigh an méid fear |
| aidedConr_0_6_16 | 5 | fa sáer oc imbirt chatha. | ag geáitsíocht sa ghleo go huasal saor | 0.7045 / 114 | aidedConr_0_10_7 | 0.5889 | dheachair dom a cheart a thabhairt |
| aidedConr_0_6_17 | 5 | Geguin tricha fer n-armach, | mharaigh tríocha laoch armtha | 0.6405 / 62 | aidedConr_0_12_66 | 0.4619 | leathan de chraiceann caorach deich n |
| aidedConr_0_6_18 | 4 | íarsin damair a marbad.” | ansin d’fhulaing an bás céanna é féin. | 0.6042 / 116 (tied 1) | aidedConr_0_4_18 | 0.3631 | é sin rampair amhra a |
| aidedConr_0_7_2 | 3 | dia n-ébrad: | dá ndúradh: | 0.5794 / 13 | aidedConr_0_12_67 | 0.4222 | deich n éadach |
| aidedConr_0_7_5 | 5 | marbais cét fer dia fairind. | Mharaigh céad dá slua. | 0.6314 / 21 | aidedConr_0_2_6 | 0.5095 | cé mharaigh an fear san mise |
| aidedConr_0_7_7 | 5 | fúair a leacht la Coinculaind.” | do chuaigh de chionn Chú Chulainn chrua. | 0.6604 / 164 | aidedConr_0_1_12 | 0.4255 | é gach uair a thionlacadh na |
| aidedConr_0_7_14 | 3 | manobáded muir mílach.” | ach gur thraoch an fharraige thréan é. | 0.6061 / 6 | aidedConr_0_7_17 | 0.5238 | lasrach thar muir |
| aidedConr_0_7_16 | 7 | .i. ó robúi oc báid fri Conchobar | Is é sin, nuair a bhí sé ag bagairt báis ar Chonchobhar | 0.6671 / 29 | aidedConr_0_4_6 | 0.5568 | shroich srúibh brain in iarthar na héireann ó ghob |
| aidedConr_0_7_19 | 6 | Mór in snám co robáided and. | B’fhada an snámh agus bádh ann é. | 0.5899 / 8 | aidedConr_0_3_1 | 0.5609 | in am an chreach a roinnt áfach |
| aidedConr_0_7_24 | 6 | ba do dígail a deigh-rígh.” | b’é ag díoghailt a dhea-rí. | 0.4806 / 9 | aidedConr_0_10_6 | 0.4095 | dúinn ar a oineach ba dheachair dom |
| aidedConr_0_8_6 | 3 | dia n-ébrad: | Fúthu san chumtaí: | 0.7746 / 247 (tied 4) | aidedConr_0_12_67 | 0.4222 | deich n éadach |
| aidedConr_0_8_8 | 4 | “Arsin tarraid cland Dedaid | Ghabh Clanna Deadhadh an cnoc aníos | 0.5726 / 13 | aidedConr_0_8_2 | 0.4629 | ansin a chaitheadar clanna deadhadh |
| aidedConr_0_8_9 | 6 | d’íaraidh a ríg da rímid, | ar thóir a rí Cú Raoi. A líon: | 0.5246 / 13 | aidedConr_0_5_16 | 0.4048 | d ardaigh sé a cheann arís d |
| aidedConr_0_8_10 | 5 | cóic fhichit ar trí chétaib | cúig scór is trí chéad | 0.5000 / 6 | aidedConr_0_8_11 | 0.3600 | trí chéad agus deich gcéad ar |
| aidedConr_0_9_3 | 4 | ocus rolasa in chathair, | is do chuir an chathair trí thine. | 0.5333 / 10 | aidedConr_0_6_2 | 0.4167 | sa chathair agus tugann an |
| aidedConr_0_9_7 | 4 | “Cóich in maccán contái | “Cén macán a chím ag athrú cló | 0.6167 / 31 (tied 3) | aidedConr_0_9_15 | 0.5042 | in éadan na carraige áfach |
| aidedConr_0_9_8 | 4 | i tóeb chathrach Conrái? | taobh le cathair Chú Raoi? | 0.6569 / 33 | aidedConr_0_5_1 | 0.4236 | i ndoras na cathrach tar |
| aidedConr_0_9_9 | 5 | Maid i mbethaid maic Dáire | Dá mba bheo mac Dháire an rí | 0.5583 / 16 | aidedConr_0_12_103 | 0.3805 | i gcomhlainn mac móraigeanta ceartchomharba dháire |
| aidedConr_0_9_10 | 5 | ní lasfed co n-imnáille.” | ní á loscadh a bheifeá mar ataoi.” | 0.5893 / 16 | aidedConr_0_12_119 | 0.5214 | in aghaidh bíobhaí ní maith do |
| aidedConr_0_9_12 | 5 | Fer Becrach didu ara Chonrúi | Mar sin, chuir Fearbheacrach, carbadóir Chú Raoi, | 0.6099 / 11 | aidedConr_0_11_4 | 0.5629 | fear eagna a chosnódh sinn lena |
| aidedConr_0_9_14 | 5 | ocus luid i carpat chuici. | Isteach leis ina charbad. | 0.5857 / 15 | aidedConr_0_12_106 | 0.5057 | a chuaigh lucht seilge i gcampa |
| aidedConr_0_9_17 | 3 | dia n-ébrad: | dá ndúradh: | 0.7460 / 181 (tied 3) | aidedConr_0_12_67 | 0.4222 | deich n éadach |
| aidedConr_0_9_19 | 4 | “Fer Becrach con-imále, | Le háilleacht is le mire | 0.6196 / 16 | aidedConr_0_2_6 | 0.5354 | mharaigh an fear san mise |
| aidedConr_0_9_20 | 4 | bés ní brég immaráide? | Fearbheacrach — gan aon agó — | 0.8504 / 272 | aidedConr_0_5_23 | 0.4556 | atáid ní haon tréad bó |
| aidedConr_0_10_2 | 6 | “Ná tú Fer Chertne?” ar Conchobar. | “Nach tusa Fearcheirtne?” d’fhiafraigh Conchobhar. | 0.6361 / 58 | aidedConr_0_1_6 | 0.4749 | mar gheall ar na trí fir ochaine |
| aidedConr_0_10_6 | 5 | “Innis dún ní dia maithis.” | “Tabhair éachtaint dúinn ar a oineach.” | 0.6895 / 119 (tied 3) | aidedConr_0_10_11 | 0.4605 | ansin adúirt fearcheirtne file ní maith |
| aidedConr_0_10_7 | 5 | “Ní ermaisim,” or seisen, “indosa. | “Ba dheachair dom a cheart a thabhairt anois dó,” arsa Fearcheirtne. | 0.8111 / 301 | aidedConr_0_10_11 | 0.5583 | adúirt fearcheirtne file ní maith do |
| aidedConr_0_10_9 | 8 | ar nom-marba íarum mo lám-sa fodén, | Is dóichí gurb í mo lámh féin a chuirfidh chun báis mé go deimhin | 0.5521 / 6 | aidedConr_0_11_3 | 0.4810 | mo naimhde ar lár an curadh calma an fear feasa |
| aidedConr_0_11_2 | 9 | ni madbui ben i tirib toruais doroscarsuid mo namuid. | monuar mura mbeadh bean a theacht i dtír ar an mbile buacach binn ó dá mbeadh mo naimhde ar lár | 0.6063 / 7 | aidedConr_0_4_20 | 0.5384 | leagtha in éirinn dob iad clanna deadhadh do ghluais i n |
| aidedConr_0_11_3 | 4 | Nar caur rus romaith | an curadh calma an fear feasa is fear eagna | 0.6536 / 96 | aidedConr_0_1_9 | 0.4923 | coire chomh maith leis na |
| aidedConr_0_11_4 | 4 | rodin fe faebra ficht | a chosnódh sinn lena chlaimhte faobhracha | 0.6577 / 33 | aidedConr_0_14_3 | 0.5667 | beara ansin chuaigh fearcheirtne le |
| aidedConr_0_11_5 | 4 | fiba fess moch mairb. | codladh an bháis tá i ndán dó feasta | 0.6944 / 95 (tied 2) | aidedConr_0_1_9 | 0.5000 | chomh maith leis na ba |
| aidedConr_0_11_7 | 5 | iar n-eraic nairc nairc | dá uireasa éagmais chinniúnach a chailliúint | 0.6978 / 168 | aidedConr_0_2_3 | 0.5167 | an uachtair air de réir mar |
| aidedConr_0_11_8 | 8 | aisndei contechgamar oen suide flsc domidsesc dond oinfer | is féidir a bhfuaireas ón aonfhear cáidh a mheas óm bhéal atá ina fhásach ceal na meá | 0.7010 / 43 | aidedConr_0_2_1 | 0.6140 | ruire chuaigh cú raoi mac dáire leosan ansin don léigear |
| aidedConr_0_11_9 | 7 | fibu iarum ailib feis iteir catha cuim.” | ina chodladh sóúil beidh feasta le linn na n-adhmholtaí a dhéantar ag gach féasta agus an sporadh a dhéantar i rith gach catha.” | 0.6714 / 68 (tied 4) | aidedConr_0_5_25 | 0.5786 | aige ar muin na bó atá ar deireadh leis |
| aidedConr_0_12_1 | 4 | “Curoi ro hir dam | “Bhronn Cú Raoi orm | 0.6583 / 66 (tied 4) | aidedConr_0_11_1 | 0.4958 | chur dem chroí monuar mura |
| aidedConr_0_12_2 | 4 | .x. mbruigi mac Daire | deich ngabháltas le clann mhac Dháire | 0.6101 / 9 (tied 1) | aidedConr_0_1_1 | 0.4786 | uladh cú raoi mac dáire |
| aidedConr_0_12_3 | 2 | .x. ndairbé, | deich gcumhal | 0.8571 / 255 (tied 199) | aidedConr_0_2_7 | 0.7143 | sheal nuair |
| aidedConr_0_12_5 | 4 | .x. n-eochu airmitiu | deich bhfíoreach | 0.6188 / 9 (tied 3) | aidedConr_0_12_85 | 0.5563 | greasta deich n alchaing arm |
| aidedConr_0_12_7 | 2 | .x. coire | deich gcoire | 0.5833 / 6 (tied 1) | aidedConr_0_1_9 | 0.5000 | tógadh coire |
| aidedConr_0_12_8 | 3 | .x. colga det | deich gcolg déadacha | 0.6667 / 8 (tied 2) | aidedConr_0_12_21 | 0.6349 | gcupa de chlocha |
| aidedConr_0_12_9 | 5 | .x. saine cernd claidhem cain | deich bpéire claimhte caoine a bheir bhua | 0.6517 / 8 | aidedConr_0_11_4 | 0.5889 | sinn lena chlaimhte faobhracha codladh an |
| aidedConr_0_12_10 | 2 | .x. mbraine | deich ngob loinge | 0.8571 / 264 (tied 136) | aidedConr_0_4_6 | 0.6429 | srúibh brain |
| aidedConr_0_12_11 | 3 | .x. mbeichluaigh buain | deich saithe de bheacha crua | 0.8222 / 257 (tied 21) | aidedConr_0_12_106 | 0.6056 | nuair a chuaigh |
| aidedConr_0_12_12 | 5 | .x. ndeich mbo bo cet | deich deich gcinn de bhuaibh | 0.6714 / 14 (tied 1) | aidedConr_0_12_13 | 0.6095 | bhuaibh deich bólacht mar tháin bó |
| aidedConr_0_12_13 | 3 | .x. mbuachailli botana | deich bólacht mar tháin bó | 0.8139 / 162 (tied 2) | aidedConr_0_12_27 | 0.6768 | bhuabhaill chóir bhronn |
| aidedConr_0_12_14 | 2 | .x. soda | deich ngadhar baineanna | 0.8571 / 99 (tied 34) | aidedConr_0_1_13 | 0.7500 | dó sa |
| aidedConr_0_12_16 | 5 | asa slabraduib findruine nó airgit | de shlabhraí fiondruine | 0.6114 / 14 (tied 1) | aidedConr_0_4_6 | 0.5684 | siad nó gur shroich srúibh brain |
| aidedConr_0_12_17 | 5 | hi sedgregaib oss n-eng. | i ndiaidh tréada damh buile. | 0.7933 / 243 (tied 3) | aidedConr_0_4_21 | 0.5533 | i n aonlá do dhéanamh na |
| aidedConr_0_12_19 | 4 | Curig ro hir dam | Dheonaigh Cú Raoi dhom | 0.5819 / 11 | aidedConr_0_3_13 | 0.5250 | raoi air chuir tríd an |
| aidedConr_0_12_20 | 2 | .x. longa | deich soitheach | 0.8889 / 173 (tied 13) | aidedConr_0_12_10 | 0.6667 | ngob loinge |
| aidedConr_0_12_21 | 4 | .x. n-ana airleic | deich gcupa de chlocha luachmhara | 0.8286 / 280 (tied 2) | aidedConr_0_5_4 | 0.5083 | bhfillfidh na sluaite lena n |
| aidedConr_0_12_22 | 2 | .x. cuacha | deich gcorn | 0.8333 / 243 (tied 115) | aidedConr_0_5_10 | 0.6667 | le clocha |
| aidedConr_0_12_24 | 3 | Ro hir dom | Bhronn orm | 0.7111 / 88 (tied 5) | aidedConr_0_12_43 | 0.4190 | airgead bheir dom |
| aidedConr_0_12_25 | 3 | .x. ngrib ingne | deich gcrúb gríbhe | 0.8111 / 80 (tied 3) | aidedConr_0_12_10 | 0.6333 | deich ngob loinge |
| aidedConr_0_12_26 | 2 | .x. mbenda | deich gcorn óil barr óir | 0.8333 / 132 (tied 106) | aidedConr_0_4_2 | 0.6429 | na mbeanna |
| aidedConr_0_12_29 | 3 | Ro ir dam | Bhronn orm | 0.6444 / 45 | aidedConr_0_1_11 | 0.5417 | do thríocha damh |
| aidedConr_0_12_30 | 2 | .x. ratha | deich ráth | 0.7000 / 12 (tied 7) | aidedConr_0_8_2 | 0.6000 | deadhadh uatha |
| aidedConr_0_12_31 | 6 | .x. treaba dagha decla alta airgither. | deich ndea-áitreabh. | 0.6986 / 24 | aidedConr_0_8_2 | 0.6473 | a chaitheadar clanna deadhadh uatha gach coirthe |
| aidedConr_0_12_34 | 4 | .x. cét oib aimind | deich gcéad de chaoirigh bhreátha | 0.7667 / 73 (tied 4) | aidedConr_0_5_7 | 0.6875 | ar muin capall cé hiad |
| aidedConr_0_12_35 | 2 | .x. fernu | deich gcrios | 0.9000 / 304 (tied 187) | aidedConr_0_12_106 | 0.7500 | m fhearann |
| aidedConr_0_12_36 | 3 | .x. eobarr óir | deich gclogad órga | 0.8690 / 264 (tied 2) | aidedConr_0_12_26 | 0.4444 | óil barr óir |
| aidedConr_0_12_37 | 4 | .x. treith tire iacih | deich dtorc tíre | 0.6375 / 8 (tied 1) | aidedConr_0_10_8 | 0.5833 | tá m intinn tréith óir |
| aidedConr_0_12_38 | 2 | .x. ndarba | deich gcumhal | 0.9167 / 319 (tied 78) | aidedConr_0_9_14 | 0.7143 | ina charbad |
| aidedConr_0_12_40 | 5 | dlongar Herion uill nó uaind. | d’fhonn Cró Choinn chloch-chruaidh a fhuirseadh | 0.7012 / 104 (tied 1) | aidedConr_0_15_3 | 0.5171 | líon a mháirseáil aduaidh trian nó |
| aidedConr_0_12_43 | 3 | Ro ir dam | bheir dom | 0.5968 / 19 | aidedConr_0_1_11 | 0.5417 | do thríocha damh |
| aidedConr_0_12_44 | 3 | .x. cumala bana | deich gcumhal ar dhath an airgid | 0.7262 / 55 | aidedConr_0_5_4 | 0.6667 | sula bhfillfidh na |
| aidedConr_0_12_45 | 3 | .x. mbuair mbecfolad | deich dtréad de stoc éadrom | 0.8704 / 282 (tied 23) | aidedConr_0_9_1 | 0.6667 | nuair a bhíodar |
| aidedConr_0_12_46 | 3 | no mbec alma | nó deich dtréad beag | 0.7111 / 73 | aidedConr_0_1_7 | 0.5714 | chluasa na mbó |
| aidedConr_0_12_49 | 3 | Ro ir dom | Dheonaigh dhom | 0.6463 / 46 (tied 1) | aidedConr_0_12_43 | 0.4857 | airgead bheir dom |
| aidedConr_0_12_51 | 5 | ro ir dom.x. mile | deich gcapall oibre | 0.6967 / 60 (tied 3) | aidedConr_0_4_17 | 0.5778 | sí comhairle do chú raoi is |
| aidedConr_0_12_52 | 2 | .x. same | deich sheisreach | 0.9000 / 281 (tied 14) | aidedConr_0_1_2 | 0.7500 | deacair san |
| aidedConr_0_12_53 | 3 | .x. coraite slabrad | deich gcuing de shlabhra breá | 0.7440 / 22 (tied 1) | aidedConr_0_12_16 | 0.6444 | de shlabhraí fiondruine |
| aidedConr_0_12_54 | 3 | sgeo glais geiliairnd. | ar a raibh glas d’iarann bán. | 0.6333 / 8 | aidedConr_0_1_10 | 0.5722 | an gcoire seo |
| aidedConr_0_12_57 | 2 | .x. ngeiltesca | deich mias réthónacha | 0.8500 / 138 (tied 124) | aidedConr_0_12_59 | 0.7500 | stropa gailleacha |
| aidedConr_0_12_58 | 3 | .x. muince doat | deich bhfáinne láimhe | 0.8083 / 182 (tied 1) | aidedConr_0_5_7 | 0.6944 | thuilleadh ar muin |
| aidedConr_0_12_60 | 3 | .x. talliama taræda | deich gcranntabhaill tine | 0.7857 / 32 | aidedConr_0_3_13 | 0.6667 | tríd an dtalamh |
| aidedConr_0_12_62 | 2 | .x. olcha | deich mbabhla dí | 0.8571 / 146 (tied 25) | aidedConr_0_4_25 | 0.6429 | déanamh folctha |
| aidedConr_0_12_63 | 3 | .x. tulcubha truma | deich gcráitéar mór groí | 0.8426 / 149 (tied 1) | aidedConr_0_10_2 | 0.7167 | sin nach tusa |
| aidedConr_0_12_64 | 2 | .x. tinnu | deich gcliathán bagúin | 0.9444 / 289 (tied 8) | aidedConr_0_3_10 | 0.7000 | fhéad éinne |
| aidedConr_0_12_65 | 2 | .x. ru | deich gclúid | 1.0000 / 321 (tied 42) | aidedConr_0_4_13 | 0.7500 | iuchna rí |
| aidedConr_0_12_66 | 3 | .x. loa lethna | deich bhfallaing leathan de chraiceann caorach | 0.7429 / 25 | aidedConr_0_6_10 | 0.6444 | díobh lena chosa |
| aidedConr_0_12_67 | 3 | .x. mbrait mbreccphupaill | deich n-éadach pubaill, | 0.8016 / 89 (tied 3) | aidedConr_0_4_6 | 0.7063 | shroich srúibh brain |
| aidedConr_0_12_68 | 4 | .x. mbruit cuinsce clithar, | deich n-éadach cosanta | 0.8019 / 196 (tied 1) | aidedConr_0_9_3 | 0.6533 | chuir an chathair trí thine |
| aidedConr_0_12_69 | 6 | condelib indeitbear fa menmain a.. nmen... | ilchruthach is éagsúil. | 0.7792 / 261 | aidedConr_0_9_21 | 0.5218 | aon agó fé ndear mac chonchobhair a |
| aidedConr_0_12_71 | 3 | Ro ir dom | Dheonaigh dom | 0.5630 / 9 | aidedConr_0_12_43 | 0.4857 | airgead bheir dom |
| aidedConr_0_12_72 | 4 | .x. n-ubla oir | deich n-úll órga | 0.6319 / 10 | aidedConr_0_5_4 | 0.5643 | na sluaite lena n ualaí |
| aidedConr_0_12_73 | 4 | .x. n-unascacha oir | deich bhfáinne cluaise órga, | 0.8576 / 307 | aidedConr_0_12_68 | 0.5556 | n éadach cosanta ilchruthach is |
| aidedConr_0_12_75 | 2 | .x. cochmedna | deich soitheach níos lú | 0.8889 / 263 (tied 144) | aidedConr_0_1_5 | 0.7778 | bhó iuchna |
| aidedConr_0_12_76 | 4 | sceo brat bidbad mBabilone | maraon le creach naimhde na Babalóine. | 0.6736 / 18 | aidedConr_0_1_12 | 0.5694 | gcuid ceoil iad mar seo |
| aidedConr_0_12_77 | 4 | .x. talliama taræda iluamand. | deich gcranntabhaill tine | 0.8403 / 263 (tied 1) | aidedConr_0_3_13 | 0.6875 | air chuir tríd an dtalamh |
| aidedConr_0_12_79 | 3 | Ro ir dom | Bhronn orm | 0.7111 / 95 (tied 5) | aidedConr_0_12_43 | 0.4857 | airgead bheir dom |
| aidedConr_0_12_80 | 3 | .x. ruchta derga | deich dtuinach dhearga | 0.7063 / 8 (tied 1) | aidedConr_0_4_24 | 0.6444 | dtrí mbó iuchna |
| aidedConr_0_12_81 | 2 | .x. mbanchaimsa | deich léine gheala | 0.9091 / 318 (tied 82) | aidedConr_0_12_62 | 0.7727 | deich mbabhla |
| aidedConr_0_12_82 | 2 | .x. cleitme | deich gclogad armasacha | 0.8571 / 217 (tied 154) | aidedConr_0_2_5 | 0.7143 | thugtaí cloigne |
| aidedConr_0_12_83 | 2 | .x. findelga | deich mbróiste ghreanta, | 0.8750 / 240 (tied 177) | aidedConr_0_1_4 | 0.7500 | bhfear fálga |
| aidedConr_0_12_84 | 5 | .x. fidchella fri luacharna lassrad | deich bhfoireann fichille greasta | 0.7092 / 9 | aidedConr_0_7_17 | 0.6746 | dhún féin ar barr lasrach thar |
| aidedConr_0_12_85 | 5 | .x. faidlenda fo a ngaiscedhuibh | deich n-alchaing arm | 0.8051 / 250 | aidedConr_0_12_40 | 0.5585 | chruaidh a fhuirseadh mar go raibh |
| aidedConr_0_12_86 | 7 | co n-iathaib aro mbui mo lantol. | oiread tailte is a shásaigh m’aigne. | 0.5952 / 11 | aidedConr_0_11_2 | 0.5306 | mbeadh mo naimhde ar lár an curadh calma an |
| aidedConr_0_12_87 | 2 | tricha aill | tríocha srian | 0.5429 / 9 (tied 1) | aidedConr_0_12_86 | 0.4429 | aigne tríocha |
| aidedConr_0_12_90 | 4 | fri heachraidhe n-ain. | le seisreach chapall án. | 0.7068 / 200 | aidedConr_0_9_1 | 0.4567 | n imghoin um an gcathair |
| aidedConr_0_12_93 | 4 | dail-sium deogaib cormaib | dháileadh orm deocha leanna | 0.6524 / 19 | aidedConr_0_14_1 | 0.5893 | sin bhuail in aghaidh carraige |
| aidedConr_0_12_94 | 3 | cuich sgeo fin | coirn fíona | 0.7333 / 193 (tied 11) | aidedConr_0_7_18 | 0.5040 | sin chuaigh sa |
| aidedConr_0_12_95 | 6 | fri mac greche con con tlus. | is cnónna a shaibhreas | 0.6806 / 57 (tied 7) | aidedConr_0_2_1 | 0.5694 | cú raoi mac dáire leosan ansin don |
| aidedConr_0_12_97 | 6 | batar fo meilgtine main medb domun | clúdaithe le bainne an duais mheisciúil a thuillidís cách | 0.6991 / 74 | aidedConr_0_15_2 | 0.6046 | ó shamhain go meán earraigh do dhealaigh |
| aidedConr_0_12_98 | 3 | do cernuib Conrui | de chionn chaithréimeanna an Chú cháidh | 0.7190 / 77 (tied 2) | aidedConr_0_1_1 | 0.4603 | do chur chun |
| aidedConr_0_12_99 | 4 | ri rondet dousairb nUltaib | d’fhulaig mo fhlaith anbhás de bharr fheara Uladh | 0.7054 / 58 | aidedConr_0_4_24 | 0.5923 | abhainn chun na nultach i |
| aidedConr_0_12_100 | 9 | ar is imaernu dessa deruich doroich sein co nue. | ar fuaid Éireann tá a cheart díoltais á agairt ar óg is aosta | 0.6040 / 73 (tied 1) | aidedConr_0_11_3 | 0.5167 | mo naimhde ar lár an curadh calma an fear feasa is |
| aidedConr_0_12_101 | 6 | Ni buanach muid amail mal Mis | níor bhuan a ghairm mar fhlaith ar Mhis | 0.6091 / 27 | aidedConr_0_1_12 | 0.5496 | na héin lena gcuid ceoil iad mar |
| aidedConr_0_12_102 | 3 | fosud acata causair. | cé gur shocair é i gcomhlainn | 0.7238 / 84 (tied 15) | aidedConr_0_10_6 | 0.5947 | sé tabhair éachtaint |
| aidedConr_0_12_103 | 8 | Cuirigh robo mor mac deo Dare dur? dianacmacht | mac móraigeanta ceartchomharba Dháire chruaidh chomhachtaigh | 0.6214 / 24 | aidedConr_0_1_1 | 0.5075 | mac dáire do chur chun báis ní deacair san mar |
| aidedConr_0_12_104 | 4 | huae cach du deguth | garmhac Dheadhadh ar gach slí | 0.6667 / 103 (tied 10) | aidedConr_0_12_66 | 0.5321 | leathan de chraiceann caorach deich |
| aidedConr_0_12_106 | 5 | Sech mo iath arrosiasair selg | nuair a chuaigh lucht seilge i gcampa lámh le m’fhearann | 0.6350 / 10 | aidedConr_0_12_99 | 0.5708 | d fhulaig mo fhlaith anbhás de |
| aidedConr_0_12_107 | 3 | a marbtha mal | nuair a mharaítí laoch | 0.4750 / 17 | aidedConr_0_15_17 | 0.3492 | mar a bhí |
| aidedConr_0_12_109 | 5 | Cuculainn consine fris Firu Ochaine | throid Cú Chulainn maol in aghaidh fhear cluas-chaithaiseacha | 0.6349 / 27 | aidedConr_0_1_7 | 0.4421 | fir ochaine is é sin éiníní |
| aidedConr_0_12_110 | 2 | huargus genair | tréan den saol rinne leac oighir | 0.7619 / 201 (tied 47) | aidedConr_0_6_7 | 0.4643 | air agus |
| aidedConr_0_12_111 | 3 | ar marbtha mnái | bean a mharaigh é | 0.7083 / 144 (tied 3) | aidedConr_0_15_14 | 0.4405 | mná brath a |
| aidedConr_0_12_112 | 4 | cen coin cin arm | ní cú ná airm | 0.6667 / 130 (tied 5) | aidedConr_0_4_1 | 0.4896 | sin bhí cú chulainn ar |
| aidedConr_0_12_113 | 4 | airm i sluagaib sin | fógraítear do na slóite sin | 0.5938 / 52 (tied 5) | aidedConr_0_5_1 | 0.3438 | sí an uair sin i |
| aidedConr_0_12_114 | 2 | sis fofuaraid | tháiníse an treo | 0.8194 / 245 (tied 11) | aidedConr_0_4_5 | 0.5000 | sin mharaigh |
| aidedConr_0_12_115 | 4 | ic nascad ara dun | bheartaís é a cheangal | 0.7685 / 311 | aidedConr_0_7_17 | 0.5387 | dhún féin ar barr lasrach |
| aidedConr_0_12_117 | 5 | mal re siabra siasair soe | fágadh ina fhlaith ar shamhlacha é | 0.7714 / 263 (tied 3) | aidedConr_0_12_15 | 0.5622 | nár dheacair a scaoileadh de shlabhraí |
| aidedConr_0_12_118 | 3 | fri riga. rogiallaid | ba ghiall é dá ríocht | 0.7833 / 195 (tied 14) | aidedConr_0_4_22 | 0.6000 | féin ina aonar |
| aidedConr_0_12_119 | 5 | robith nie namait. et cetera. | ba churadh é in aghaidh bíobhaí | 0.7476 / 161 (tied 3) | aidedConr_0_4_22 | 0.6000 | na cathrach go dtí nach raibh |
| aidedConr_0_13_1 | 7 | “Is rígda in tabairt sein,” ar Conchobar. | “B’shiúd é an t-oineach rí,” ar Conchobhar. | 0.4816 / 9 | aidedConr_0_4_22 | 0.3663 | ina aonar ina chathair ar an lá sin is |
| aidedConr_0_13_2 | 8 | “Is bec deiseom anní sin,” ar Fer Chertne. | “Uaidh siúd ba bheagsan,” ar Fearcheirtne. | 0.5662 / 47 | aidedConr_0_1_6 | 0.3756 | ar na trí fir ochaine is é sin éiníní beaga |
| aidedConr_0_13_4 | 5 | “Atá sund,” ar innd óic, | “Tá sí anseo,” ar na h-óglaigh. | 0.5667 / 21 (tied 3) | aidedConr_0_5_25 | 0.4000 | bó atá ar deireadh leis sin |
| aidedConr_0_13_5 | 12 | “ocus is íar mbeim a chind do Choinrúi il-lúag a tesarcthi.” | “De chionn a tarrthála a teascadh an ceann de Chú Raoi.” | 0.4914 / 13 | aidedConr_0_9_3 | 0.4625 | a cheann den fhear is do chuir an chathair trí thine bhí fearcheirtne file chú |
| aidedConr_0_14_3 | 7 | Bert íarum intí Fer Chertne róthar chuici | Ansin chuaigh Fearcheirtne le báiní ansin dá hionsaí. | 0.6207 / 16 (tied 1) | aidedConr_0_9_3 | 0.5660 | a cheann den fhear is do chuir an chathair |
| aidedConr_0_14_4 | 6 | ocus nongeb iter a dí láim | D’iaigh a ghéaga ina timpeall | 0.6274 / 62 | aidedConr_0_15_17 | 0.5417 | láimh sin mar a bhí ag oidhe |
| aidedConr_0_14_7 | 5 | co darobrúi in charrac diblínaib | gur bhris an charraig iad araon. | 0.6306 / 29 | aidedConr_0_9_15 | 0.5321 | ina charbad thiomáin na heacha in |
| aidedConr_0_14_8 | 8 | co fil al-lecht forsin tráig fon carraic. | Ar an gcladach fé bhun an lia tá a liag. | 0.6750 / 127 | aidedConr_0_9_3 | 0.5521 | do chuir an chathair trí thine bhí fearcheirtne file chú |
| aidedConr_0_14_9 | 3 | Is de rochét: | Tugtar anso a bhfeartlaoi: | 0.8864 / 317 | aidedConr_0_9_19 | 0.4333 | le háilleacht is |
| aidedConr_0_14_11 | 4 | “Trúag in comroc imale | Ba thruamhéileach an comhlann i gcomhar | 0.6518 / 49 | aidedConr_0_12_109 | 0.5250 | throid cú chulainn maol in |
| aidedConr_0_14_13 | 5 | co fil al-leacht diblínaib | uaigh na beirte acu sé áit atá | 0.7220 / 208 | aidedConr_0_6_7 | 0.5222 | fir a theach air agus go |
| aidedConr_0_15_1 | 8 | Aropaidi roás ind n-imguin foraib cách día | D’ainneoin sin, ba i líonmhaire a chuaigh a maraíodh díobh gach lá, | 0.6990 / 176 | aidedConr_0_9_1 | 0.5513 | mhíle ach nuair a bhíodar á n imghoin um an |
| aidedConr_0_15_3 | 10 | Roármiset Ulaid dia tig fén oc dul ocus ic tuideacht | Do dhealaigh na hUltaigh an méid fear a réitigh chun filleadh ó thuaidh ón líon a mháirseáil aduaidh. | 0.7067 / 146 | aidedConr_0_4_23 | 0.6161 | do sochraíodh eatarthu idir í féin agus cú chulainn i tál de |
| aidedConr_0_15_5 | 1 | condébairt: | go ndúradh: | 0.7000 / 145 (tied 92) | aidedConr_0_9_13 | 0.5000 | chonchobhair |
| aidedConr_0_15_8 | 5 | ba holc a gnim dogena | b’í a rinne feillghníomh. | 0.6167 / 95 (tied 2) | aidedConr_0_1_12 | 0.4473 | a thionlacadh na héin lena gcuid |
| aidedConr_0_15_9 | 5 | Sech ní terna i segha | Cé nár tháinig saor í féin | 0.6950 / 142 | aidedConr_0_5_1 | 0.4900 | i ndoras na cathrach tar sa |
| aidedConr_0_15_10 | 5 | fagbus Erna fo mela, E | na hÉarainn d’fhág fé náire mo léan. | 0.7017 / 68 (tied 1) | aidedConr_0_5_10 | 0.5381 | agus le daracha do dhéanamh na |
| aidedConr_0_15_13 | 4 | la horcain ós Aircedglind. | sa tsléacht in Airgeadghleann. | 0.6259 / 13 | aidedConr_0_4_9 | 0.5617 | srúibh brain is é a |
| aidedConr_0_15_15 | 4 | dáig is fris rodamidir.” | a fir nuair atá féna láimh. | 0.6708 / 57 | aidedConr_0_4_8 | 0.4972 | áit i srúibh brain is |
| aidedConr_0_15_17 | 4 | Aiged tra Conrúi andsin. | Sin mar a bhí ag Oidhe Chú Raoi. | 0.6500 / 45 (tied 8) | aidedConr_0_4_12 | 0.4667 | ansin óir bhí grá aige |
| aidedDiar_0_1_9 | 9 | ochtar for loch do théigedh.i. do chuaid Ciarán | Bhí Ciarán ag teacht le hochtar ar an loch | 0.5761 / 46 | aidedDiar_0_21_25 | 0.4769 | loch do fhomna déise mar shéan aonair nífidh macha do |
| aidedDiar_0_2_5 | 5 | atbertsat a dráidhi fri Diarmait: | Dúirt a dhraoithe le Diarmaid: | 0.4917 / 10 | aidedDiar_0_4_32 | 0.4060 | a chléirigh arsa diarmaid breith |
| aidedDiar_0_2_6 | 12 | “in ní dia fataigter in teni út anocht ní báidfigter” ar siat. | “Tá a leithéid de chúis le hadú na tine seo anocht nach múchfar í choíche.” | 0.6176 / 75 (tied 2) | aidedDiar_0_6_9 | 0.5184 | ina dhiaidh sin ina rí ar éirinn agus níor tháinig san am úd |
| aidedDiar_0_2_7 | 5 | “bud hinnoss ón” or Diarmait | “Anois a dhéanfar sin,” arsa Diarmaid | 0.5679 / 8 (tied 1) | aidedDiar_0_4_14 | 0.5250 | diarmaid ós rud é gur |
| aidedDiar_0_3_1 | 12 | Is ann sin búi in clérech ic sádhud eculsa in tan sin. | Bhí an cléireach ag sá-bhunú eaglaise ansiúd ag an am. | 0.6178 / 101 | aidedDiar_0_20_8 | 0.4804 | colm cille is uaidh sin a lean an t ainm ann i cúil |
| aidedDiar_0_3_2 | 5 | “cissi hopair dogní?” or Diarmait. | “Cad tá ar siúl agat?” arsa Diarmaid. | 0.6117 / 25 (tied 4) | aidedDiar_0_30_12 | 0.4907 | d iompaig diarmaid ar ais |
| aidedDiar_0_3_8 | 8 | for feraib Erenn sul bus tráthsa nach noirrther.” | ar fhir Éireann roimh an tráth seo amanathar.” | 0.6060 / 10 | aidedDiar_0_13_19 | 0.5676 | is fíor seo arsa diarmaid mise an crann agus |
| aidedDiar_0_3_9 | 5 | “cinnus dogéntar ón?” ar Diarmait: | “Conas a dhéanfar sin?” arsa Diarmaid, | 0.5250 / 20 (tied 3) | aidedDiar_0_20_6 | 0.4333 | ar diarmaid ansin is in |
| aidedDiar_0_3_12 | 7 | “is folaidh dia in nísin” ol Ciarán. | “Sin é gnó Dé,” arsa Ciarán. | 0.5935 / 64 | aidedDiar_0_20_6 | 0.4457 | briseadh ar diarmaid ansin is in aghaidh |
| aidedDiar_0_3_16 | 4 | co farcaib cin anmain. | agus d’fhág ar lár marbh é. | 0.8140 / 526 | aidedDiar_0_5_11 | 0.4762 | diarmaid do chiarán ansin |
| aidedDiar_0_3_22 | 13 | ro rígsat iarum fir Eirenn in tí Diarmaíd siu ro bo cenn sechtmaini. | Rinne fir Éireann ansin Diarmaid a ríogadh sula raibh an tseachtain slán. | 0.5728 / 9 | aidedDiar_0_4_1 | 0.5365 | uisnigh le diarmaid agus le fir éireann um bealtaine mar ba iad trí ard |
| aidedDiar_0_4_2 | 9 | ár roptar iat trí harddála Erenn issin aimsir sin | mar ba iad trí ard-dála Éireann an t-am úd ná | 0.5661 / 9 | aidedDiar_0_25_1 | 0.5263 | sin ar a chuairt rí deiseal éireann óir is mar |
| aidedDiar_0_4_6 | 10 | ocus cid bé no ticedh tairrsib sin ó feraib Erenn | agus cibé d’fhir Éireann a choillfeadh iadsan, | 0.6857 / 242 | aidedDiar_0_25_3 | 0.4965 | teamhrach féile éireann i ó theamhair go laighin agus as sin |
| aidedDiar_0_4_7 | 10 | ba bidba báis in tí no milledh in cáin sin. | a bhrisfeadh an dlí sin, bhí breith bháis air. | 0.5400 / 11 | aidedDiar_0_23_11 | 0.4979 | lá do bháis féin arsa colm cille tá a fhios sin |
| aidedDiar_0_4_10 | 5 | ocus búi i comnaide and. | agus rinne sos nó cónaí ann | 0.5917 / 44 (tied 5) | aidedDiar_0_6_7 | 0.4667 | agus bhi sé ansiúd i |
| aidedDiar_0_4_13 | 6 | “cid fil and tra” ar Diarmait: | “Sea, anois, más ea,” arsa Diarmaid, | 0.7042 / 441 (tied 2) | aidedDiar_0_3_2 | 0.4306 | an am cad tá ar siúl |
| aidedDiar_0_4_14 | 6 | “ár is ann so ro cétcomraicseam | “ós rud é gur anseo a chasamar ar a chéile don chéad uair | 0.6984 / 282 (tied 5) | aidedDiar_0_25_2 | 0.4802 | is mar seo a chaitheadh rí |
| aidedDiar_0_4_15 | 6 | iar ngabáil ríghe damsa triat bennachtainsi | tar éis dom an ríocht a bhaint amach trí do bheannachtsa, | 0.6323 / 18 | aidedDiar_0_3_3 | 0.5811 | ag tógáil eaglaise bige arsa ciarán |
| aidedDiar_0_4_19 | 7 | bái náma do’n rígh isin magh | Bhí namhaid don rí ar an machaire | 0.5995 / 23 | aidedDiar_0_24_13 | 0.5190 | bheidh ar do phláta ní dócha sin |
| aidedDiar_0_4_23 | 4 | ocus gontar astigh é. | agus goineadh Díoma istigh ann; | 0.5417 / 18 (tied 4) | aidedDiar_0_30_11 | 0.4583 | é ag cur ga |
| aidedDiar_0_4_30 | 6 | bid sí sin aidhed do gébasa | gurb í sin an íde a gheobhaidh tusa | 0.6111 / 47 (tied 7) | aidedDiar_0_18_7 | 0.5000 | sin í d imigh siad uaidh |
| aidedDiar_0_4_33 | 3 | “do óighriar duit.” | “breith do bhéil féin duit.” | 0.4722 / 8 (tied 2) | aidedDiar_0_8_25 | 0.2500 | do bhéal duit |
| aidedDiar_0_4_35 | 5 | rotngona de mina tegba samlaid.” | gur de a ghoinfear mé mura dtarlaíonn amhaidh.” | 0.5870 / 10 | aidedDiar_0_30_5 | 0.5521 | iontais faoi rinnead teach de |
| aidedDiar_0_4_36 | 9 | conad de do rat bás Diarmata amail ro tarrngairedh. | Uime sin a thug sé bás Dhiarmada chun críche mar a tairngreadh. | 0.5765 / 19 | aidedDiar_0_3_20 | 0.4935 | ea maol mór ba dhuine de thriúr comhalta do dhiarmaid |
