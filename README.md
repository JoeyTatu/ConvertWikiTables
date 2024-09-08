# ConvertWikiTables
Converts one line wikicode tables into multiple lines using Python.

You will need an input file which is ```input_wiki_code.txt``` in this converter.py file.

It will convert (e.g.) 

```
  {| class="wikitable sortable" style="font-size: 90%; text-align: center; width: 100%;"
  ! rowspan="2" width="10%"|'''Date'''
  ! colspan="2" width="20%"|'''Affects'''
  ! rowspan="2" width="5%" |'''Current EPG number'''
  ! rowspan="2" width="10%"|'''Current channel logo'''
  ! rowspan="2" width="10%"|'''Current channel name'''
  ! rowspan="2" width="10%"|'''Type of change'''
  ! rowspan="2" width="5%" |'''New EPG number'''
  ! rowspan="2" width="10%"|'''New channel logo'''
  ! rowspan="2" width="10%"|'''New channel name'''
  ! rowspan="2" width="10%"|'''References/Notes'''
  |-
  ! width="10%"|'''Region'''
  ! width="01%"|'''Devices''' <!-- 10+20+5+10+10+10+5+10+10+10 -->
  |-
  |rowspan="3"|01/01/24||||||304||Sky Cinema Favourites {{Res|HD}}||rowspan="3" bgcolor="#ffc299"|Reversion||||Sky Cinema Greats {{Res|HD}}||
  |-
  |||{{SkyQ}}||849||Sky Cinema Favourites {{Res|SD}}||||Sky Cinema Greats {{Res|SD}}||
  |-
  |||||302||Sky Cinema Christmas {{Res|HD}}||||Sky Cinema Drama {{Res|HD}}||
  |-
  |rowspan="2"|02/01/24||rowspan="2"| ||{{SkyQ}}||605||rowspan="2"|Nick SpongeBob {{Res|SD}}||rowspan="2" bgcolor="#ffc299"|Reversion||rowspan="2"| ||rowspan="2"|Nicktoons {{Res|SD}} || rowspan="2"| 
  |-
  |bgcolor="#b3ffff"|{{SkyGlass}}||205
  |-
  |rowspan="21"|03/01/24||UK||rowspan="2"|{{SkyQ}}||159||rowspan="4"|E! {{Res|HD}}||rowspan="6" bgcolor="#ff4d4d"|Removal||rowspan="6"| ||rowspan="6"| ||rowspan="6"| 
  |-
  |Ire||348
  |-
  |Eng, Scot, NI||rowspan="2" bgcolor="#b3ffff"|{{SkyGlass}}||117
  |-
  |Wales, Ire||118
  |-
  |UK||rowspan="2"|{{SkyQ}}||835||rowspan="2"|E! {{Res|SD}}
  |-
  |Ire||159
  |-
  |rowspan="2"|Wales||rowspan="2" bgcolor="#b3ffff"|{{SkyGlass}}||119||BBC Three {{Res|HD}}||rowspan="2" bgcolor="#ff99c2"|Move||118||rowspan="2"| ||rowspan="2"| 
  |-
  |120||BBC Four {{Res|HD}}||119
  |-
  |||{{SkyQ}}||181||Channel 7 {{Res|SD}}||bgcolor="#9999ff"|Restoration||||||
  |-
  |||||303||Sky Cinema Wizarding World {{Res|HD}}||bgcolor="#fff099"|Temporary rename||||Sky Cinema Fast & Furious {{Res|HD}}||
  |-
  |||||302||Sky Cinema Drama {{Res|HD}}||rowspan="3" bgcolor="#ff99c2"|Move||310||||
  |-
  |||||303||Sky Cinema Fast & Furious {{Res|HD}}||302||||
  |-
  |||||310||Sky Cinema Hits {{Res|HD}}||303||||
  |-
  |rowspan="2"| ||bgcolor="#b3ffff"|{{SkyGlass}}||317||GREAT! Christmas {{Res|HD}}||rowspan="3" bgcolor="#ffc299"|Reversion||rowspan="3"| ||GREAT! romance {{Res|HD}}||rowspan="3"| 
  |-
  |rowspan="2"|{{SkyQ}}||319||GREAT! Christmas {{Res|SD}}||GREAT! romance {{Res|SD}}
  |-
  |UK||320||GREAT! Christmas {{Res|+1}}||GREAT! romance {{Res|+1}}
  |-
  |rowspan="5"|UK||||355||BoXmas {{Res|SD}}||rowspan="2" bgcolor="#ffc299"|Reversion||||The Box {{Res|SD}}||
  |-
  |rowspan="4"|{{SkyQ}}||366||Best Xmas Music {{Res|SD}}||||That's 80s {{Res|SD}}||
  |-
  |188||That's Christmas {{Res|SD}}||bgcolor="#ffe866"|Rename||||That's TV 2 {{Res|SD}}||
  |-
  |366||That's 80s {{Res|SD}}||rowspan="2" bgcolor="#ff99c2"| Move||360||||
  |-
  |367||That's 90s {{Res|SD}}||366||||
  |-
  |rowspan="2"|04/01/24||||||408||Sky Sports Darts {{Res|HD}}||rowspan="2" bgcolor="#ffc299"|Reversion||||Sky Sports Arena {{Res|HD}}||
  |-
  |||{{SkyQ}}||866||Sky Sports Darts {{Res|SD}}||||Sky Sports Arena {{Res|SD}}||
  |-
  |05/01/24||||||303||Sky Cinema Hits {{Res|HD}}||bgcolor="#fff099"|Temporary rename||||Sky Cinema Superman {{Res|HD}}||
  |-
  |rowspan="4"|06/01/24||rowspan="4"| ||{{SkyQ}}||325||rowspan="2"|Christmas 24 {{Res|SD}}||rowspan="4" bgcolor="#ffc299"|Reversion||rowspan="4"| ||rowspan="2"|Movies 24 {{Res|SD}}||rowspan="4"| 
  |-
  |bgcolor="#b3ffff"|{{SkyGlass}}||313
  |-
  |{{SkyQ}}||326||rowspan="2"|Christmas 24+ {{Res|SD}}||rowspan="2"|Movies 24+ {{Res|SD}}
  |-
  |bgcolor="#b3ffff"|{{SkyGlass}}||314
  |-
  |rowspan="4"|08/01/24||||||308||Sky Cinema Ultimate Comedy {{Res|HD}}||rowspan="2" bgcolor="#ffc299"|Reversion||||Sky Cinema Comedy {{Res|HD}}||
  |-
  |||||303||Sky Cinema Superman {{Res|HD}}||||Sky Cinema Hits {{Res|HD}}||
  |-
  |||||304||Sky Cinema Greats {{Res|HD}}||rowspan="2" bgcolor="#fff099"|Temporary rename||||Sky Cinema Cult Classics {{Res|HD}}||
  |-
  |||{{SkyQ}}||849||Sky Cinema Greats {{Res|SD}}||||Sky Cinema Cult Classics {{Res|SD}}||
  |-
  |rowspan="14"|09/01/24||ScotB||rowspan="14"|{{SkyQ}}||rowspan="6"|803||ITV1 {{Res|SD}}<br><small>(Border Scotland)</small>||rowspan="9" bgcolor="#ff4d4d"|Removal||||||
  |-
  |CI||ITV1 {{Res|SD}}<br><small>(Channel TV)</small>||||||
  |-
  |Wales||ITV1 {{Res|SD}}<br><small>(Wales)</small>||||||
  |-
  |NI||UTV {{Res|SD}}||||||
  |-
  |West Scotland <br> <small> (Glasgow)</small>||STV West <br><small> (Glasgow)</small> {{Res|SD}}||||||
  |-
  |North Scotland <br> <small> (Dundee)</small>||STV North <br><small> (Dundee)</small> {{Res|SD}}||||||
  |-
  |rowspan="3"|UK||817||ITV3 {{Res|SD}}||||||
  |-
  |818||ITV4 {{Res|SD}}||||||
  |-
  |843||ITVBe {{Res|SD}}||||||
  |-
  |ScotB, NI||rowspan="5"|803||ITV1 {{Res|SD}}<br><small>(Granada)</small>||rowspan="5" bgcolor="#4dff4d"|Launch||||||
  |-
  |Wales||ITV1 {{Res|SD}}<br><small>(Central West)</small>||||||
  |-
  |CI||ITV1 {{Res|SD}}<br><small>(Meridian East)</small>||||||
  |-
  |West Scotland <br> <small> (Glasgow)</small>||STV East {{Res|SD}}<br><small>(Edinburgh)</small>||||||
  |-
  |North Scotland <br> <small> (Dundee)</small>||STV North {{Res|SD}}<br><small>(Aberdeen)</small>||||||
  |-
  |15/01/24||||||302||Sky Cinema Fast & Furious {{Res|HD}}||bgcolor="#fff099"|Temporary rename||||Sky Cinema Feel Good {{Res|HD}}||
  |-
  |rowspan="3"|18/01/24||rowspan="2"|Border England<br><small>(Region 12)</small>||rowspan="3"|{{SkyQ}}||rowspan="2"|103||ITV1 {{Res|HD}}<br><small>(Border Scotland)</small>||bgcolor="#ff4d4d"|Removal||||||
  |-
  |ITV1 {{Res|HD}}<br><small>(Border England)</small>||bgcolor="#9999ff"|Restoration||||||
  |-
  |UK||0134||Khushkhabri 🔊||bgcolor="#ff8080"|Temporary removal||||||
  |-
  |rowspan="2"|19/01/24||||||304||Sky Cinema Cult Classics {{Res|HD}}||rowspan="2" bgcolor="#ffc299"|Reversion||||Sky Cinema Greats {{Res|HD}}||
  |-
  |||{{SkyQ}}||849||Sky Cinema Cult Classics {{Res|SD}}||||Sky Cinema Greats {{Res|SD}}||
  |-
  |22/01/24||||||303||Sky Cinema Hits {{Res|HD}}||bgcolor="#fff099"|Temporary rename||||Sky Cinema Star Trek {{Res|HD}}||
  |-
  |rowspan="2"|23/01/24||||{{SkyQ}}||712||Foodxp {{Res|SD}}||rowspan="2" bgcolor="#ffe866"|Rename||||Dangal {{Res|SD}}||
  |-
  |||bgcolor="#b3ffff"|{{SkyGlass}}||715||Foodxp {{Res|HD}}||||Dangal {{Res|HD}}||
  |-
  |24/01/24||UK||{{SkyQ}}||0134||Khushkhabri 🔊||bgcolor="#9999ff"|Restoration||||||
  |-
  |rowspan="5"|25/01/24||rowspan="5"|UK||rowspan="5"|{{SkyQ}}||412||Viaplay Sports 1 {{Res|HD}}||rowspan="2" bgcolor="#ff99c2"|Move||419||rowspan="3"| ||rowspan="3"| 
  |-
  |419||Viaplay Sports 2 {{Res|HD}}||420
  |-
  |420||Viaplay Xtra {{Res|HD}}||rowspan="3" bgcolor="#ff4d4d"|Removal||
  |-
  |rowspan="2"|no number||BBC Alba (SID 6446) {{Res|SD}}||||||rowspan="2"|Previously used for secondary audio
  |-
  |BBC Alba (SID 8927) {{Res|HD}}||||
  |-
  |rowspan="14"|29/01/24||UK||rowspan="14"|{{SkyQ}}||801||rowspan="2"|BBC One {{Res|SD}}<br><small>(Nightlight)</small>||rowspan="14" bgcolor="#ff4d4d"|Removal||rowspan="14"| ||rowspan="14"| ||rowspan="14"|On 8 January, the channels were replaced with a slate informing viewers that the channel had been closed and of alternative arrangements to view channel.
  Channels were removed from SD boxes on 26 March 2024.
  |-
  |Ire||832
  |-
  |UK||802||rowspan="2"|BBC Two {{Res|SD}}
  |-
  |Ire||844
  |-
  |||845||BBC Three {{Res|SD}}
  |-
  |UK||815||rowspan="2"|BBC Four {{Res|SD}}
  |-
  |Ire||833
  |-
  |rowspan="5"|UK||847||BBC Alba {{Res|SD}}
  |-
  |844||BBC Scotland {{Res|SD}}
  |-
  |882||BBC News {{Res|SD}}
  |-
  |887||BBC Parliament {{Res|SD}}
  |-
  |971||BBC Red Button 1 {{Res|SD}}
  |-
  |rowspan="2"| ||643||CBBC {{Res|SD}}
  |-
  |644||CBeebies {{Res|SD}}
  
  |}
```

into:

```
  {| class="wikitable sortable" style="font-size: 90%; text-align: center; width: 100%;"
  ! rowspan="2" width="10%"|'''Date'''
  ! colspan="2" width="20%"|'''Affects'''
  ! rowspan="2" width="5%" |'''Current EPG number'''
  ! rowspan="2" width="10%"|'''Current channel logo'''
  ! rowspan="2" width="10%"|'''Current channel name'''
  ! rowspan="2" width="10%"|'''Type of change'''
  ! rowspan="2" width="5%" |'''New EPG number'''
  ! rowspan="2" width="10%"|'''New channel logo'''
  ! rowspan="2" width="10%"|'''New channel name'''
  ! rowspan="2" width="10%"|'''References/Notes'''
  |-
  ! width="10%"|'''Region'''
  ! width="01%"|'''Devices''' <!-- 10+20+5+10+10+10+5+10+10+10 -->
  |-
  |rowspan="3"|01/01/24
  |
  |
  |304
  |Sky Cinema Favourites {{Res|HD}}
  |rowspan="3" bgcolor="#ffc299"|Reversion
  |
  |Sky Cinema Greats {{Res|HD}}|
  |-
  |{{SkyQ}}
  |849
  |Sky Cinema Favourites {{Res|SD}}
  |
  |Sky Cinema Greats {{Res|SD}}|
  |-
  |
  |302
  |Sky Cinema Christmas {{Res|HD}}
  |
  |Sky Cinema Drama {{Res|HD}}|
  |-
  |rowspan="2"|02/01/24
  |rowspan="2"| 
  |{{SkyQ}}
  |605
  |rowspan="2"|Nick SpongeBob {{Res|SD}}
  |rowspan="2" bgcolor="#ffc299"|Reversion
  |rowspan="2"| 
  |rowspan="2"|Nicktoons {{Res|SD}} | rowspan="2"| 
  |-
  |bgcolor="#b3ffff"|{{SkyGlass}}
  |205
  |-
  |rowspan="21"|03/01/24
  |UK
  |rowspan="2"|{{SkyQ}}
  |159
  |rowspan="4"|E! {{Res|HD}}
  |rowspan="6" bgcolor="#ff4d4d"|Removal
  |rowspan="6"| 
  |rowspan="6"| 
  |rowspan="6"| 
  |-
  |Ire
  |348
  |-
  |Eng, Scot, NI
  |rowspan="2" bgcolor="#b3ffff"|{{SkyGlass}}
  |117
  |-
  |Wales, Ire
  |118
  |-
  |UK
  |rowspan="2"|{{SkyQ}}
  |835
  |rowspan="2"|E! {{Res|SD}}
  |-
  |Ire
  |159
  |-
  |rowspan="2"|Wales
  |rowspan="2" bgcolor="#b3ffff"|{{SkyGlass}}
  |119
  |BBC Three {{Res|HD}}
  |rowspan="2" bgcolor="#ff99c2"|Move
  |118
  |rowspan="2"| 
  |rowspan="2"| 
  |-
  |120
  |BBC Four {{Res|HD}}
  |119
  |-
  |{{SkyQ}}
  |181
  |Channel 7 {{Res|SD}}
  |bgcolor="#9999ff"|Restoration
  |
  |
  |-
  |
  |303
  |Sky Cinema Wizarding World {{Res|HD}}
  |bgcolor="#fff099"|Temporary rename
  |
  |Sky Cinema Fast & Furious {{Res|HD}}|
  |-
  |
  |302
  |Sky Cinema Drama {{Res|HD}}
  |rowspan="3" bgcolor="#ff99c2"|Move
  |310
  |
  |-
  |
  |303
  |Sky Cinema Fast & Furious {{Res|HD}}
  |302
  |
  |-
  |
  |310
  |Sky Cinema Hits {{Res|HD}}
  |303
  |
  |-
  |rowspan="2"| 
  |bgcolor="#b3ffff"|{{SkyGlass}}
  |317
  |GREAT! Christmas {{Res|HD}}
  |rowspan="3" bgcolor="#ffc299"|Reversion
  |rowspan="3"| 
  |GREAT! romance {{Res|HD}}
  |rowspan="3"| 
  |-
  |rowspan="2"|{{SkyQ}}
  |319
  |GREAT! Christmas {{Res|SD}}
  |GREAT! romance {{Res|SD}}
  |-
  |UK
  |320
  |GREAT! Christmas {{Res|+1}}
  |GREAT! romance {{Res|+1}}
  |-
  |rowspan="5"|UK
  |
  |355
  |BoXmas {{Res|SD}}
  |rowspan="2" bgcolor="#ffc299"|Reversion
  |
  |The Box {{Res|SD}}|
  |-
  |rowspan="4"|{{SkyQ}}
  |366
  |Best Xmas Music {{Res|SD}}
  |
  |That's 80s {{Res|SD}}|
  |-
  |188
  |That's Christmas {{Res|SD}}
  |bgcolor="#ffe866"|Rename
  |
  |That's TV 2 {{Res|SD}}|
  |-
  |366
  |That's 80s {{Res|SD}}
  |rowspan="2" bgcolor="#ff99c2"| Move
  |360
  |
  |-
  |367
  |That's 90s {{Res|SD}}
  |366
  |
  |-
  |rowspan="2"|04/01/24
  |
  |
  |408
  |Sky Sports Darts {{Res|HD}}
  |rowspan="2" bgcolor="#ffc299"|Reversion
  |
  |Sky Sports Arena {{Res|HD}}|
  |-
  |{{SkyQ}}
  |866
  |Sky Sports Darts {{Res|SD}}
  |
  |Sky Sports Arena {{Res|SD}}|
  |-
  |05/01/24
  |
  |
  |303
  |Sky Cinema Hits {{Res|HD}}
  |bgcolor="#fff099"|Temporary rename
  |
  |Sky Cinema Superman {{Res|HD}}|
  |-
  |rowspan="4"|06/01/24
  |rowspan="4"| 
  |{{SkyQ}}
  |325
  |rowspan="2"|Christmas 24 {{Res|SD}}
  |rowspan="4" bgcolor="#ffc299"|Reversion
  |rowspan="4"| 
  |rowspan="2"|Movies 24 {{Res|SD}}
  |rowspan="4"| 
  |-
  |bgcolor="#b3ffff"|{{SkyGlass}}
  |313
  |-
  |{{SkyQ}}
  |326
  |rowspan="2"|Christmas 24+ {{Res|SD}}
  |rowspan="2"|Movies 24+ {{Res|SD}}
  |-
  |bgcolor="#b3ffff"|{{SkyGlass}}
  |314
  |-
  |rowspan="4"|08/01/24
  |
  |
  |308
  |Sky Cinema Ultimate Comedy {{Res|HD}}
  |rowspan="2" bgcolor="#ffc299"|Reversion
  |
  |Sky Cinema Comedy {{Res|HD}}|
  |-
  |
  |303
  |Sky Cinema Superman {{Res|HD}}
  |
  |Sky Cinema Hits {{Res|HD}}|
  |-
  |
  |304
  |Sky Cinema Greats {{Res|HD}}
  |rowspan="2" bgcolor="#fff099"|Temporary rename
  |
  |Sky Cinema Cult Classics {{Res|HD}}|
  |-
  |{{SkyQ}}
  |849
  |Sky Cinema Greats {{Res|SD}}
  |
  |Sky Cinema Cult Classics {{Res|SD}}|
  |-
  |rowspan="14"|09/01/24
  |ScotB
  |rowspan="14"|{{SkyQ}}
  |rowspan="6"|803
  |ITV1 {{Res|SD}}<br><small>(Border Scotland)</small>
  |rowspan="9" bgcolor="#ff4d4d"|Removal
  |
  |
  |-
  |CI
  |ITV1 {{Res|SD}}<br><small>(Channel TV)</small>
  |
  |
  |-
  |Wales
  |ITV1 {{Res|SD}}<br><small>(Wales)</small>
  |
  |
  |-
  |NI
  |UTV {{Res|SD}}
  |
  |
  |-
  |West Scotland <br> <small> (Glasgow)</small>
  |STV West <br><small> (Glasgow)</small> {{Res|SD}}
  |
  |
  |-
  |North Scotland <br> <small> (Dundee)</small>
  |STV North <br><small> (Dundee)</small> {{Res|SD}}
  |
  |
  |-
  |rowspan="3"|UK
  |817
  |ITV3 {{Res|SD}}
  |
  |
  |-
  |818
  |ITV4 {{Res|SD}}
  |
  |
  |-
  |843
  |ITVBe {{Res|SD}}
  |
  |
  |-
  |ScotB, NI
  |rowspan="5"|803
  |ITV1 {{Res|SD}}<br><small>(Granada)</small>
  |rowspan="5" bgcolor="#4dff4d"|Launch
  |
  |
  |-
  |Wales
  |ITV1 {{Res|SD}}<br><small>(Central West)</small>
  |
  |
  |-
  |CI
  |ITV1 {{Res|SD}}<br><small>(Meridian East)</small>
  |
  |
  |-
  |West Scotland <br> <small> (Glasgow)</small>
  |STV East {{Res|SD}}<br><small>(Edinburgh)</small>
  |
  |
  |-
  |North Scotland <br> <small> (Dundee)</small>
  |STV North {{Res|SD}}<br><small>(Aberdeen)</small>
  |
  |
  |-
  |15/01/24
  |
  |
  |302
  |Sky Cinema Fast & Furious {{Res|HD}}
  |bgcolor="#fff099"|Temporary rename
  |
  |Sky Cinema Feel Good {{Res|HD}}|
  |-
  |rowspan="3"|18/01/24
  |rowspan="2"|Border England<br><small>(Region 12)</small>
  |rowspan="3"|{{SkyQ}}
  |rowspan="2"|103
  |ITV1 {{Res|HD}}<br><small>(Border Scotland)</small>
  |bgcolor="#ff4d4d"|Removal
  |
  |
  |-
  |ITV1 {{Res|HD}}<br><small>(Border England)</small>
  |bgcolor="#9999ff"|Restoration
  |
  |
  |-
  |UK
  |0134
  |Khushkhabri 🔊
  |bgcolor="#ff8080"|Temporary removal
  |
  |
  |-
  |rowspan="2"|19/01/24
  |
  |
  |304
  |Sky Cinema Cult Classics {{Res|HD}}
  |rowspan="2" bgcolor="#ffc299"|Reversion
  |
  |Sky Cinema Greats {{Res|HD}}|
  |-
  |{{SkyQ}}
  |849
  |Sky Cinema Cult Classics {{Res|SD}}
  |
  |Sky Cinema Greats {{Res|SD}}|
  |-
  |22/01/24
  |
  |
  |303
  |Sky Cinema Hits {{Res|HD}}
  |bgcolor="#fff099"|Temporary rename
  |
  |Sky Cinema Star Trek {{Res|HD}}|
  |-
  |rowspan="2"|23/01/24
  |
  |{{SkyQ}}
  |712
  |Foodxp {{Res|SD}}
  |rowspan="2" bgcolor="#ffe866"|Rename
  |
  |Dangal {{Res|SD}}|
  |-
  |bgcolor="#b3ffff"|{{SkyGlass}}
  |715
  |Foodxp {{Res|HD}}
  |
  |Dangal {{Res|HD}}|
  |-
  |24/01/24
  |UK
  |{{SkyQ}}
  |0134
  |Khushkhabri 🔊
  |bgcolor="#9999ff"|Restoration
  |
  |
  |-
  |rowspan="5"|25/01/24
  |rowspan="5"|UK
  |rowspan="5"|{{SkyQ}}
  |412
  |Viaplay Sports 1 {{Res|HD}}
  |rowspan="2" bgcolor="#ff99c2"|Move
  |419
  |rowspan="3"| 
  |rowspan="3"| 
  |-
  |419
  |Viaplay Sports 2 {{Res|HD}}
  |420
  |-
  |420
  |Viaplay Xtra {{Res|HD}}
  |rowspan="3" bgcolor="#ff4d4d"|Removal|
  |-
  |rowspan="2"|no number
  |BBC Alba (SID 6446) {{Res|SD}}
  |
  |
  |rowspan="2"|Previously used for secondary audio
  |-
  |BBC Alba (SID 8927) {{Res|HD}}
  |
  |-
  |rowspan="14"|29/01/24
  |UK
  |rowspan="14"|{{SkyQ}}
  |801
  |rowspan="2"|BBC One {{Res|SD}}<br><small>(Nightlight)</small>
  |rowspan="14" bgcolor="#ff4d4d"|Removal
  |rowspan="14"| 
  |rowspan="14"| 
  |rowspan="14"|On 8 January, the channels were replaced with a slate informing viewers that the channel had been closed and of alternative arrangements to view channel.
  Channels were removed from SD boxes on 26 March 2024.
  |-
  |Ire
  |832
  |-
  |UK
  |802
  |rowspan="2"|BBC Two {{Res|SD}}
  |-
  |Ire
  |844
  |-
  |845
  |BBC Three {{Res|SD}}
  |-
  |UK
  |815
  |rowspan="2"|BBC Four {{Res|SD}}
  |-
  |Ire
  |833
  |-
  |rowspan="5"|UK
  |847
  |BBC Alba {{Res|SD}}
  |-
  |844
  |BBC Scotland {{Res|SD}}
  |-
  |882
  |BBC News {{Res|SD}}
  |-
  |887
  |BBC Parliament {{Res|SD}}
  |-
  |971
  |BBC Red Button 1 {{Res|SD}}
  |-
  |rowspan="2"| 
  |643
  |CBBC {{Res|SD}}
  |-
  |644
  |CBeebies {{Res|SD}}
  |}
```
