from django.db import models


# Define the dictionaries for Regions, Categories, variables, and counties ( one per region)

REGION = (
    ('1', 'I Region'),
    ('2', 'II Region'),
    ('3', 'III region'),
    ('4', 'IV Region'),
    ('5', 'V Region'),
    ('6', 'VI Region'),
    ('7', 'VII Region'),
    ('8', 'VIII Region'),
    ('9', 'IX Region'),
    ('10', 'X Region'),
    ('11', 'XI Region'),
    ('12', 'XII Region'),
    ('13', 'XIII Region'),
   )

CAT = (
    ('1', 'poverty'),
    ('2','income'),
    )

VAR = (

    ('1', 'education'),
    ('2','employment'),
)

C1=(

('1101', 'iquique'), ('1107', 'alto hospicio'),

)

C2 = (

('2101', 'antofagasta'), ('2102', 'mejillones'), ('2103', 'sierra gorda'),
('2104', 'taltal'), ('2201', 'calama'), ('2203', 'san pedro de atacama'),
('2301', 'tocopilla'), ('2302', 'maria elena'),

)

C3 = (

('3101', 'copiapo'), ('3102', 'caldera'), ('3103', 'tierra amarilla'),
 ('3201', 'chanaral'), ('3202', 'diego de almagro'), ('3301', 'vallenar'),
 ('3302', 'alto del carmen'), ('3303', 'freirina'), ('3304', 'huasco'),

 )

C4 = (

 ('4101', 'la serena'), ('4102', 'coquimbo'), ('4103', 'andacollo'),
 ('4104', 'la higuera'), ('4105', 'paiguano'), ('4106', 'vicuna'), ('4201', 'illapel'),
 ('4202', 'canela'), ('4203', 'los vilos'), ('4204', 'salamanca'), ('4301', 'ovalle'),
 ('4302', 'combarbala'), ('4303', 'monte patria'), ('4304', 'punitaqui'),
 ('4305', 'rio hurtado'),

 )


C5 =(('5101', 'valparaiso'), ('5102', 'casablanca'), ('5103', 'concon'),
('5105', 'puchuncavi'), ('5107', 'quintero'), ('5109', 'vina del mar'),
('5301', 'los andes'), ('5302', 'calle larga'), ('5303', 'rinconada'),
('5304', 'san esteban'), ('5401', 'la ligua'), ('5402', 'cabildo'),
('5403', 'papudo'), ('5404', 'petorca'), ('5405', 'zapallar'),
('5501', 'quillota'), ('5502', 'calera'), ('5503', 'hijuelas'),
('5504', 'la cruz'), ('5506', 'nogales'), ('5601', 'san antonio'),
('5602', 'algarrobo'), ('5603', 'cartagena'), ('5604', 'el quisco'),
('5605', 'el tabo'), ('5606', 'santo domingo'), ('5701', 'san felipe'),
('5702', 'catemu'), ('5703', 'llaillay'), ('5704', 'panquehue'),
('5705', 'putaendo'), ('5706', 'santa maria'),
)

C6 =(
('6101', 'rancagua'), ('6102', 'codegua'), ('6103', 'coinco'),
('6104', 'coltauco'), ('6105', 'donihue'), ('6106', 'graneros'),
('6107', 'las cabras'), ('6108', 'machali'), ('6109', 'malloa'),
('6110', 'mostazal'), ('6111', 'olivar'), ('6112', 'peumo'),
('6113', 'pichidegua'), ('6114', 'quinta de tilcoco'), ('6115', 'rengo'),
('6116', 'requinoa'), ('6117', 'san vicente'), ('6201', 'pichilemu'),
('6202', 'la estrella'), ('6203', 'litueche'), ('6204', 'marchihue'),
('6205', 'navidad'), ('6206', 'paredones'), ('6301', 'san fernando'),
('6302', 'chepica'), ('6303', 'chimbarongo'), ('6304', 'lolol'),
('6305', 'nancagua'), ('6306', 'palmilla'), ('6307', 'peralillo'),
('6308', 'placilla'), ('6309', 'pumanque'), ('6310', 'santa cruz'),

)

C7 =(

('7101', 'talca'), ('7102', 'constitucion'), ('7103', 'curepto'),
('7104', 'empedrado'), ('7105', 'maule'), ('7106', 'pelarco'),
('7107', 'pencahue'), ('7108', 'rio claro'), ('7109', 'san clemente'),
('7110', 'san rafael'), ('7201', 'cauquenes'), ('7202', 'chanco'),
('7203', 'pelluhue'), ('7301', 'curico'), ('7302', 'hualane'),
('7303', 'licanten'), ('7304', 'molina'), ('7305', 'rauco'),
('7306', 'romeral'), ('7307', 'sagrada familia'), ('7308', 'teno'),
('7309', 'vichuquen'), ('7401', 'linares'), ('7402', 'colbun'),
('7403', 'longavi'), ('7404', 'parral'), ('7405', 'retiro'),
('7406', 'san javier'), ('7407', 'villa alegre'), ('7408', 'yerbas buenas'),

)

C8 = (

('8101', 'concepcion'), ('8102', 'coronel'), ('8103', 'chiguayante'),
('8104', 'florida'), ('8105', 'hualqui'), ('8106', 'lota'),
('8107', 'penco'), ('8108', 'san pedro de la paz'), ('8109', 'santa juana'),
('8110', 'talcahuano'), ('8111', 'tome'), ('8112', 'hualpen'), ('8201', 'lebu'),
('8202', 'arauco'), ('8203', 'canete'), ('8204', 'contulmo'),
('8205', 'curanilahue'), ('8206', 'los alamos'), ('8207', 'tirua'),
('8301', 'los angeles'), ('8302', 'antuco'), ('8303', 'cabrero'),
('8304', 'laja'), ('8305', 'mulchen'), ('8306', 'nacimiento'),
('8307', 'negrete'), ('8308', 'quilaco'), ('8309', 'quilleco'),
('8310', 'san rosendo'), ('8311', 'santa barbara'), ('8312', 'tucapel'),
('8313', 'yumbel'), ('8314', 'alto biobio'), ('8401', 'chillan'),
('8402', 'bulnes'), ('8403', 'cobquecura'), ('8404', 'coelemu'),
('8405', 'coihueco'), ('8406', 'chillan viejo'), ('8407', 'el carmen'),
 ('8408', 'ninhue'), ('8409', 'niquen'), ('8410', 'pemuco'),
 ('8411', 'pinto'), ('8412', 'portezuelo'), ('8413', 'quillon'),
 ('8414', 'quirihue'), ('8415', 'ranquil'), ('8416', 'san carlos'),
 ('8417', 'san fabian'), ('8418', 'san ignacio'), ('8419', 'san nicolas'),
 ('8420', 'treguaco'), ('8421', 'yungay'),

 )


C9 =(
('9101', 'temuco'), ('9102', 'carahue'), ('9103', 'cunco'), ('9104', 'curarrehue'),
('9105', 'freire'), ('9106', 'galvarino'), ('9107', 'gorbea'), ('9108', 'lautaro'),
 ('9109', 'loncoche'), ('9110', 'melipeuco'), ('9111', 'nueva imperial'),
 ('9112', 'padre las casas'), ('9113', 'perquenco'), ('9114', 'pitrufquen'),
 ('9115', 'pucon'), ('9116', 'saavedra'), ('9117', 'teodoro schmidt'), ('9118', 'tolten'),
 ('9119', 'vilcun'), ('9120', 'villarrica'), ('9121', 'cholchol'), ('9201', 'angol'),
 ('9202', 'collipulli'), ('9203', 'curacautin'), ('9204', 'ercilla'), ('9205', 'lonquimay'),
  ('9206', 'los sauces'), ('9207', 'lumaco'), ('9208', 'puren'), ('9209', 'renaico'),
  ('9210', 'traiguen'), ('9211', 'victoria')
  )


C10 = (

('10101', 'puerto montt'), ('10102', 'calbuco'), ('10104', 'fresia'),
('10105', 'frutillar'), ('10106', 'los muermos'), ('10107', 'llanquihue'),
('10108', 'maullin'), ('10109', 'puerto varas'), ('10201', 'castro'),
('10202', 'ancud'), ('10203', 'chonchi'), ('10204', 'curaco de velez'),
('10205', 'dalcahue'), ('10206', 'puqueldon'), ('10207', 'queilen'),
('10208', 'quellon'), ('10209', 'quemchi'), ('10210', 'quinchao'),
('10301', 'osorno'), ('10302', 'puerto octay'), ('10303', 'purranque'),
('10304', 'puyehue'), ('10305', 'rio negro'), ('10306', 'san juan de la costa'),
 ('10307', 'san pablo'),

 )



C11 = (

('11101', 'coyhaique'), ('11201', 'aysen'), ('11202', 'cisnes'),
('11301', 'cochrane'), ('11401', 'chile chico'), ('11402', 'rio ibanez'),

)



C12 = (

('12101', 'punta arenas'), ('12301', 'porvenir'), ('12401', 'natales'),

)


C13 = (
('13101', 'santiago'),
('13102', 'cerrillos'),
 ('13103', 'cerro navia'),
 ('13104', 'conchali'),
 ('13105', 'el bosque'),
 ('13106', 'estacion central'),
 ('13107', 'huechuraba'),
 ('13108', 'independencia'),
 ('13109', 'la cisterna'),
 ('13110', 'la florida'),
 ('13111', 'la granja'),
 ('13112', 'la pintana'),
 ('13113', 'la reina'),
 ('13114', 'las condes'),
 ('13115', 'lo barnechea'),
 ('13116', 'lo espejo'),
 ('13117', 'lo prado'),
 ('13118', 'macul'), ('13119', 'maipu'), ('13120', 'nunoa'), ('13121', 'pedro aguirre cerda'),
 ('13122', 'penalolen'), ('13123', 'providencia'), ('13124', 'pudahuel'), ('13125', 'quilicura'),
 ('13126', 'quinta normal'), ('13127', 'recoleta'), ('13128', 'renca'), ('13129', 'san joaquin'),
 ('13130', 'san miguel'), ('13131', 'san ramon'), ('13132', 'vitacura'), ('13201', 'puente alto'),
 ('13202', 'pirque'), ('13203', 'san jose de maipo'), ('13301', 'colina'), ('13302', 'lampa'),
 ('13303', 'tiltil'), ('13401', 'san bernardo'), ('13402', 'buin'), ('13403', 'calera de tango'),
  ('13404', 'paine'), ('13501', 'melipilla'), ('13502', 'alhue'), ('13503', 'curacavi'),
  ('13504', 'maria pinto'), ('13505', 'san pedro'), ('13601', 'talagante'), ('13602', 'el monte'),
  ('13603', 'isla de maipo'), ('13604', 'padre hurtado'), ('13605', 'penaflor'),
  )





REGION_DICT = dict(REGION)
CAT_DICT = dict(CAT)
VAR_DICT = dict(VAR)

C1_DICT =dict(C1)
C2_DICT =dict(C2)
C3_DICT =dict(C3)
C4_DICT =dict(C4)
C5_DICT =dict(C5)
C6_DICT =dict(C6)
C7_DICT =dict(C7)
C8_DICT =dict(C8)
C9_DICT = dict(C9)
C10_DICT = dict(C10)
C11_DICT = dict(C11)
C12_DICT = dict(C12)
C13_DICT = dict(C13)

# Defines the models

class Input(models.Model):

    region = models.CharField(max_length=2, choices=REGION)
    cat = models.CharField(max_length=1, choices=CAT)
    edu_pov  = models.CharField(max_length=1, choices=VAR)

    c1 = models.CharField(max_length=5, choices=C1)
    c2 = models.CharField(max_length=5, choices=C2)
    c3 = models.CharField(max_length=5, choices=C3)
    c4 = models.CharField(max_length=5, choices=C4)
    c5 = models.CharField(max_length=5, choices=C5)
    c6 = models.CharField(max_length=5, choices=C6)
    c7 = models.CharField(max_length=5, choices=C7)
    c8 = models.CharField(max_length=5, choices=C8)
    c9 = models.CharField(max_length=5, choices=C9)
    c10 = models.CharField(max_length=5, choices=C10)
    c11 = models.CharField(max_length=5, choices=C11)
    c12 = models.CharField(max_length=5, choices=C12)
    c13 = models.CharField(max_length=5, choices=C13)
    name  = models.CharField(max_length=50)
