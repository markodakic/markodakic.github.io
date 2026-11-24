# Objavljivanje web-stranice — korak po korak

Tvoj GitHub username je `markodakic` i konačna adresa je https://markodakic.github.io/.

## A. Kreiranje repozitorija (ti u GitHub webu)

1. Otvori https://github.com/new i prijavi se kao **markodakic**.
2. Owner: `markodakic`.
3. Repository name: **markodakic.github.io** (točno tako, s točkama).
4. Visibility: **Public**.
5. Označi **Add a README file** kako bi nastala `main` grana.
6. Klikni **Create repository**.
7. Vrati se u ChatGPT i napiši: **Repozitorij je kreiran.** Povezani GitHub alat može tada preuzeti upload, ovisno o dozvolama pristupa.

## B. Alternativa: samostalni upload

Ako je jednostavnije, raspakiraj ZIP. Na početnoj stranici repozitorija klikni **Add file → Upload files**. Povuci datoteke iznutra mape `marko-portfolio-v3` u korijen repozitorija. Najvažnije su `index.html`, `style.css`, `script.js`, `work.html`, `articles.html`, `cases/`, `content/`, `assets/`. Sačuvaj i `.github` i `.pages.yml` ako želiš kasnije uređivanje članaka kroz CMS. Potvrdi **Commit changes**.

**Pazi:** `index.html` mora biti na razini repozitorija; NE u mapi `marko-portfolio-v3/`.

## C. Uključivanje GitHub Pagesa

1. Otvori `https://github.com/markodakic/markodakic.github.io/settings/pages`.
2. U **Build and deployment** → **Source** odaberi **Deploy from a branch**.
3. Branch: **main**; folder: **/(root)**.
4. Klikni **Save**.
5. Nakon završene objave provjeri `https://markodakic.github.io/`, `https://markodakic.github.io/work.html` i `https://markodakic.github.io/articles.html`.

Ako vidiš 404, provjeri je li u rootu datoteka `index.html`, je li grana `main`, te status objave pod **Actions** ili **Settings → Pages**.

## D. Dodavanje tvoje fotografije

1. Odaberi profesionalnu, ali prirodnu fotografiju — svijetlo i blagi osmijeh, bez stroge korporativne poze.
2. Kadriraj lice i ramena u okomiti omjer 4:5, oko 900 × 1125 px.
3. Spremi datoteku pod nazivom **profile.jpg**, veličina idealno 250–500 KB.
4. U GitHubu je dodaj u **assets/profile.jpg**. Inicijali MD automatski se zamjenjuju fotografijom.

Ne objavljuj fotografiju neke druge osobe niti AI ilustraciju kao vlastiti portret.

## E. Članci i kućni eksperimenti

- Poveznica **Articles & Lab / Članci i Lab** već je u glavnom izborniku.
- Prvi dvojezični nacrt o privatnom Cloud PC-ju dostupan je **odvojeno od javnog GitHub ZIP-a**. Tako njegovi tekstovi nisu javno vidljivi dok ih ne pregledaš i odobriš.
- Dok u `content/articles.json` nema objavljenog članka, na webu je vidljiva sekcija s temama koje planiraš istraživati.
- Kad pregledaš tekst, možemo ga prenijeti iz privatnog nacrta u `content/articles.json`, postaviti `published: true` i izgraditi stranicu `articles/my-personal-cloud-pc.html`. GitHub Actions će ju automatski izgraditi nakon spremanja podataka.
- Za budući članak napravi novi objekt s jedinstvenim `id` u `content/articles.json`, popuni naslov/sažetak/odjeljke na oba jezika, i objavi kada je gotov.
- Na LinkedInu objavi kratku osobnu objavu s poveznicom na cijeli članak na svojoj web-stranici, umjesto LinkedIn Articles.

## F. Prije dijeljenja stranice recruiterima

- Provjeri email, LinkedIn URL i sve javne case studyje, posebno tvrdnje o rezultatima.
- Otvori stranicu na telefonu i desktopu.
- Tek zatim u LinkedIn **Featured / Istaknuto** dodaj poveznicu na `https://markodakic.github.io/`.

