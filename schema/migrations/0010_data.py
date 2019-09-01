from django.db import migrations

def forwards_func(apps, schema_editor):
  # We get the model from the versioned app registry;
  # if we directly import it, it'll be the wrong version
  db_alias = schema_editor.connection.alias

  Manufacturer = apps.get_model("schema", "Manufacturer")
  Manufacturer.objects.using(db_alias).bulk_create([
    Manufacturer(name="Boots", city="Nottingham", country="England", url="http://www.boots.com/", founded="1849"),
    Manufacturer(name="Braun", city="Nuremberg", country="Germany", url="http://www.braun-phototechnik.de/", founded="1915"),
    Manufacturer(name="Canon", city="Tokyo", country="Japan", url="http://www.canon.com/", founded="1937"),
    Manufacturer(name="Standard Cameras", country="England", founded="1931"),
    Manufacturer(name="Efke", city="Samobor", country="Croatia", founded="1947", dissolved="2012"),
    Manufacturer(name="Fuji", city="Tokyo", country="Japan", url="http://www.fujifilm.com/", founded="1934"),
    Manufacturer(name="Halina", country="China", founded="1906"),
    Manufacturer(name="Homemade", country="England"),
    Manufacturer(name="Ilford", city="Ilford", country="England", url="http://www.ilfordphoto.com/", founded="1879"),
    Manufacturer(name="KMZ", city="Krasnogorsk", country="Russia", url="http://www.zenit-foto.ru/", founded="1942"),
    Manufacturer(name="Kodak", city="Rochester", country="USA", url="http://www.kodak.com/", founded="1892"),
    Manufacturer(name="LOMO", city="St. Petersburg", country="Russia", url="http://www.lomoplc.com/", founded="1932", dissolved="1914"),
    Manufacturer(name="Maco", country="Germany", url="http://www.maco-photo.de/"),
    Manufacturer(name="Makinon", city="Tokyo", country="Japan", founded="1967", dissolved="1985"),
    Manufacturer(name="Mamiya", city="Tokyo", country="Japan", url="http://www.mamiyaleaf.com/", founded="1940"),
    Manufacturer(name="Olympus", city="Tokyo", country="Japan", url="http://www.olympus.co.uk/", founded="1919"),
    Manufacturer(name="Opteka", country="Japan", founded="2002"),
    Manufacturer(name="Samyang", city="Masan", country="South Korea", url="http://www.syopt.co.kr/", founded="1972"),
    Manufacturer(name="Tamron", city="Saitama", country="Japan", url="http://www.tamron.co.jp/en/", founded="1950"),
    Manufacturer(name="Unknown"),
    Manufacturer(name="Voigtlander", city="Vienna", country="Austria", url="http://www.voigtlaender.de/", founded="1756"),
    Manufacturer(name="Tokina", country="Japan", url="http://www.tokinalens.com/", founded="1970"),
    Manufacturer(name="Kenko", city="Tokyo", country="Japan", url="http://www.kenko-tokina.co.jp/e/index.html", founded="1928"),
    Manufacturer(name="Paragon", country="Japan"),
    Manufacturer(name="Agfa", city="Berlin", country="Germany", founded="1867"),
    Manufacturer(name="LPL", country="Japan", url="http://www.lpl-web.co.jp/", founded="1953"),
    Manufacturer(name="Durst", country="Italy", founded="1936"),
    Manufacturer(name="Toshikato", country="Japan"),
    Manufacturer(name="Vivitar", country="USA", url="http://www.vivitar.com/", founded="1938"),
    Manufacturer(name="Tudor", country="Japan"),
    Manufacturer(name="Rollei", city="Braunschweig", country="Germany", url="http://www.rollei.com/", founded="1920"),
    Manufacturer(name="Komamura", country="Japan", founded="1933"),
    Manufacturer(name="Ensign", city="London", country="England", founded="1903"),
    Manufacturer(name="Ross", city="London", country="England", founded="1830"),
    Manufacturer(name="Kentmere", city="Kentmere", country="England", url="http://www.kentmere.co.uk/"),
    Manufacturer(name="Jessops", city="Leicester", country="England", url="http://www.jessops.com/", founded="1935"),
    Manufacturer(name="Cosina", city="Nakano", country="Japan", url="http://www.cosina.co.jp/seihin/voigt/english/", founded="1959"),
    Manufacturer(name="Manfrotto", city="Cassola", country="Italy", url="http://www.manfrotto.co.uk/", founded="1974"),
    Manufacturer(name="Pentax", city="Tokyo", country="Japan", url="http://www.pentax.co.uk/", founded="1919"),
    Manufacturer(name="Blazzeo", country="China"),
    Manufacturer(name="Cobra"),
    Manufacturer(name="Sunpak", country="Japan", url="http://www.sunpak.jp/english/", founded="1963"),
    Manufacturer(name="Miranda", country="Japan", founded="1955"),
    Manufacturer(name="Hanimex", country="Australia", founded="1947"),
    Manufacturer(name="Ohnar", country="Japan"),
    Manufacturer(name="Celestron", country="USA", url="http://www.celestron.com/", founded="1964"),
    Manufacturer(name="Sigma", country="Japan", url="http://www.sigma-imaging-uk.com/", founded="1961"),
    Manufacturer(name="Lancaster", country="England", founded="1835"),
    Manufacturer(name="Schneider-Kreuznach", country="Germany", url="http://www.schneiderkreuznach.com/foto_e/foto", founded="1913"),
    Manufacturer(name="Leitz", country="Germany", url="http://uk.leica-camera.com/home/", founded="1913"),
    Manufacturer(name="Aldis", country="England", founded="1901"),
    Manufacturer(name="Revelation", country="Taiwan"),
    Manufacturer(name="Pentacon", city="Dresden", country="Germany", url="http://www.pentacon-dresden.de/", founded="1959"),
    Manufacturer(name="Chinon", city="Nagano", country="Japan", url="http://www.chinon.co.jp/", founded="1948", dissolved="2004"),
    Manufacturer(name="Dollond & Newcombe", country="England"),
    Manufacturer(name="Loonar Goupe", country="China"),
    Manufacturer(name="Polaroid", country="USA", url="http://www.polaroid.com/", founded="1937"),
    Manufacturer(name="The Impossible Project", city="Enschede", country="Netherlands", url="https://www.the-impossible-project.com/", founded="2008"),
    Manufacturer(name="Lomography", country="Austria", url="http://www.lomography.com/", founded="1992"),
    Manufacturer(name="Yongnuo", country="China", url="http://en.yongnuo.com.cn/"),
    Manufacturer(name="Graflex", country="USA", url="http://graflex.org/", founded="1898"),
    Manufacturer(name="Tokyo Kogaku", country="Japan", url="http://www.topcon.co.jp/en/index.html", founded="1932"),
    Manufacturer(name="Linhof", country="Germany", url="http://www.linhof.com/index-e.html", founded="1887"),
    Manufacturer(name="De Vere", country="England"),
    Manufacturer(name="Nikon", city="Tokyo", country="Japan", url="http://www.nikkor.com/", founded="1932"),
    Manufacturer(name="Konica", city="Tokyo", country="Japan", founded="1873", dissolved="2003"),
    Manufacturer(name="Feinwerk Technik", country="Germany"),
    Manufacturer(name="Meopta", city="Bratislava", country="Slovakia", founded="1933"),
    Manufacturer(name="ORWO", city="Wolfen", country="Germany", url="http://www.filmotec.de/"),
    Manufacturer(name="Fotospeed", city="Corsham", country="England", url="http://www.fotospeed.com/"),
    Manufacturer(name="Shackman", city="London", country="England"),
    Manufacturer(name="Dallmeyer", country="England", founded="1860"),
    Manufacturer(name="Sekonic"),
    Manufacturer(name="Zeiss Ikon", country="Germany"),
    Manufacturer(name="Realt", country="France"),
    Manufacturer(name="Soligor", city="Stuttgart", country="Germany", founded="1968"),
    Manufacturer(name="Bowens", city="London", country="England", founded="1923"),
    Manufacturer(name="Optomax", country="Japan"),
    Manufacturer(name="Philips", country="Holland", founded="1891"),
    Manufacturer(name="Bausch & Lomb"),
    Manufacturer(name="Bell & Howell"),
    Manufacturer(name="Kitvision", country="UK"),
    Manufacturer(name="MDT"),
    Manufacturer(name="Jacquard", country="USA", founded="1988"),
    Manufacturer(name="Neewer", country="China"),
    Manufacturer(name="Holga"),
    Manufacturer(name="Kawauso-Shoten", country="Japan"),
    Manufacturer(name="Minolta"),
    Manufacturer(name="Roeschlein-Kreuznach", country="Germany"),
    Manufacturer(name="Staeble", country="Germany", founded="1908"),
    Manufacturer(name="Tetenal"),
    Manufacturer(name="Foma"),
    Manufacturer(name="Tucht", city="Dusseldorf", country="Germany"),
    Manufacturer(name="Rodenstock", country="Germany"),
    Manufacturer(name="Roniflex"),
  ])
    

def reverse_func(apps, schema_editor):
  db_alias = schema_editor.connection.alias

  Manufacturer = apps.get_model("schema", "Manufacturer")
  Manufacturer.objects.using(db_alias).filter(name="Boots")
  Manufacturer.objects.using(db_alias).filter(name="Braun")
  Manufacturer.objects.using(db_alias).filter(name="Canon")
  Manufacturer.objects.using(db_alias).filter(name="Standard Cameras")
  Manufacturer.objects.using(db_alias).filter(name="Efke")
  Manufacturer.objects.using(db_alias).filter(name="Fuji")
  Manufacturer.objects.using(db_alias).filter(name="Halina")
  Manufacturer.objects.using(db_alias).filter(name="Homemade")
  Manufacturer.objects.using(db_alias).filter(name="Ilford")
  Manufacturer.objects.using(db_alias).filter(name="KMZ")
  Manufacturer.objects.using(db_alias).filter(name="Kodak")
  Manufacturer.objects.using(db_alias).filter(name="LOMO")
  Manufacturer.objects.using(db_alias).filter(name="Maco")
  Manufacturer.objects.using(db_alias).filter(name="Makinon")
  Manufacturer.objects.using(db_alias).filter(name="Mamiya")
  Manufacturer.objects.using(db_alias).filter(name="Olympus")
  Manufacturer.objects.using(db_alias).filter(name="Opteka")
  Manufacturer.objects.using(db_alias).filter(name="Samyang")
  Manufacturer.objects.using(db_alias).filter(name="Tamron")
  Manufacturer.objects.using(db_alias).filter(name="Unknown")
  Manufacturer.objects.using(db_alias).filter(name="Voigtlander")
  Manufacturer.objects.using(db_alias).filter(name="Tokina")
  Manufacturer.objects.using(db_alias).filter(name="Kenko")
  Manufacturer.objects.using(db_alias).filter(name="Paragon")
  Manufacturer.objects.using(db_alias).filter(name="Agfa")
  Manufacturer.objects.using(db_alias).filter(name="LPL")
  Manufacturer.objects.using(db_alias).filter(name="Durst")
  Manufacturer.objects.using(db_alias).filter(name="Toshikato")
  Manufacturer.objects.using(db_alias).filter(name="Vivitar")
  Manufacturer.objects.using(db_alias).filter(name="Tudor")
  Manufacturer.objects.using(db_alias).filter(name="Rollei")
  Manufacturer.objects.using(db_alias).filter(name="Komamura")
  Manufacturer.objects.using(db_alias).filter(name="Ensign")
  Manufacturer.objects.using(db_alias).filter(name="Ross")
  Manufacturer.objects.using(db_alias).filter(name="Kentmere")
  Manufacturer.objects.using(db_alias).filter(name="Jessops")
  Manufacturer.objects.using(db_alias).filter(name="Cosina")
  Manufacturer.objects.using(db_alias).filter(name="Manfrotto")
  Manufacturer.objects.using(db_alias).filter(name="Pentax")
  Manufacturer.objects.using(db_alias).filter(name="Blazzeo")
  Manufacturer.objects.using(db_alias).filter(name="Cobra")
  Manufacturer.objects.using(db_alias).filter(name="Sunpak")
  Manufacturer.objects.using(db_alias).filter(name="Miranda")
  Manufacturer.objects.using(db_alias).filter(name="Hanimex")
  Manufacturer.objects.using(db_alias).filter(name="Ohnar")
  Manufacturer.objects.using(db_alias).filter(name="Celestron")
  Manufacturer.objects.using(db_alias).filter(name="Sigma")
  Manufacturer.objects.using(db_alias).filter(name="Lancaster")
  Manufacturer.objects.using(db_alias).filter(name="Schneider-Kreuznach")
  Manufacturer.objects.using(db_alias).filter(name="Leitz")
  Manufacturer.objects.using(db_alias).filter(name="Aldis")
  Manufacturer.objects.using(db_alias).filter(name="Revelation")
  Manufacturer.objects.using(db_alias).filter(name="Pentacon")
  Manufacturer.objects.using(db_alias).filter(name="Chinon")
  Manufacturer.objects.using(db_alias).filter(name="Dollond & Newcombe")
  Manufacturer.objects.using(db_alias).filter(name="Loonar Goupe")
  Manufacturer.objects.using(db_alias).filter(name="Polaroid")
  Manufacturer.objects.using(db_alias).filter(name="The Impossible Project")
  Manufacturer.objects.using(db_alias).filter(name="Lomography")
  Manufacturer.objects.using(db_alias).filter(name="Yongnuo")
  Manufacturer.objects.using(db_alias).filter(name="Graflex")
  Manufacturer.objects.using(db_alias).filter(name="Tokyo Kogaku")
  Manufacturer.objects.using(db_alias).filter(name="Linhof")
  Manufacturer.objects.using(db_alias).filter(name="De Vere")
  Manufacturer.objects.using(db_alias).filter(name="Nikon")
  Manufacturer.objects.using(db_alias).filter(name="Konica")
  Manufacturer.objects.using(db_alias).filter(name="Feinwerk Technik")
  Manufacturer.objects.using(db_alias).filter(name="Meopta")
  Manufacturer.objects.using(db_alias).filter(name="ORWO")
  Manufacturer.objects.using(db_alias).filter(name="Fotospeed")
  Manufacturer.objects.using(db_alias).filter(name="Shackman")
  Manufacturer.objects.using(db_alias).filter(name="Dallmeyer")
  Manufacturer.objects.using(db_alias).filter(name="Sekonic")
  Manufacturer.objects.using(db_alias).filter(name="Zeiss Ikon")
  Manufacturer.objects.using(db_alias).filter(name="Realt")
  Manufacturer.objects.using(db_alias).filter(name="Soligor")
  Manufacturer.objects.using(db_alias).filter(name="Bowens")
  Manufacturer.objects.using(db_alias).filter(name="Optomax")
  Manufacturer.objects.using(db_alias).filter(name="Philips")
  Manufacturer.objects.using(db_alias).filter(name="Bausch & Lomb")
  Manufacturer.objects.using(db_alias).filter(name="Bell & Howell")
  Manufacturer.objects.using(db_alias).filter(name="Kitvision")
  Manufacturer.objects.using(db_alias).filter(name="MDT")
  Manufacturer.objects.using(db_alias).filter(name="Jacquard")
  Manufacturer.objects.using(db_alias).filter(name="Neewer")
  Manufacturer.objects.using(db_alias).filter(name="Holga")
  Manufacturer.objects.using(db_alias).filter(name="Kawauso-Shoten")
  Manufacturer.objects.using(db_alias).filter(name="Minolta")
  Manufacturer.objects.using(db_alias).filter(name="Roeschlein-Kreuznach")
  Manufacturer.objects.using(db_alias).filter(name="Staeble")
  Manufacturer.objects.using(db_alias).filter(name="Tetenal")
  Manufacturer.objects.using(db_alias).filter(name="Foma")
  Manufacturer.objects.using(db_alias).filter(name="Tucht")
  Manufacturer.objects.using(db_alias).filter(name="Rodenstock")
  Manufacturer.objects.using(db_alias).filter(name="Roniflex")
  


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0009_auto_20190901_2033')
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
