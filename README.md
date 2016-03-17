# CS Games — Official Results / Résultats officiels
This is an archive of the official results of the CS Games.

Ceci est une archive des résultats officiels des CS Games.

# Structure
<dl>
	<dt><code>{year / année}/csv/</code></dt><dd>
		Data for a particular year as CSV files. /
		Données d’une année en particulier sous la forme de fichiers CSV.
	</dd>
	<dt><code>{year / année}/csv/compscores.csv</code></dt><dd>
		Data of the <code>compscores</code> table. /
		Données de la table <code>compscores</code>.
	</dd>
	<dt><code>{year / année}/csv/delegations.csv</code></dt><dd>
		Data of the <code>delegations</code> table. /
		Données de la table <code>delegations</code>.
	</dd>
	<dt><code>{year}/en/</code></dt><dd>English web pages</dd>
	<dt><code>{année}/fr/</code></dt><dd>Pages web francophones</dd>
	<dt><code>{year / année}/{en|fr}/overall.html</code></dt><dd>
		Résultats globaux (<code>http://csgames.org/registration/?page=scores&lang=…</code>)
	</dd>
	<dt><code>{year / année}/{en|fr}/registration.html</code></dt><dd>
		Liste des équipes (<code>http://csgames.org/registration/?lang=…</code>)
	</dd>
	<dt><code>README.md</code></dt><dd>This file / Ce fichier</dd>
	<dt><code>to-csv.py</code></dt><dd>
		Extracts data from the archived web pages and store them as CSV files. /
		Extrait les données depuis les pages web archivés et les enregistre sous
		la forme de fichiers CSV.
	</dd>
	<dt><code>University</code></dt><dd>
		<p>Content of the <code>University</code> table and aliases.
		When multiple rows have the same ID, only the first one is stored
		in the database and the others are used to fix university names of the
		raw data.</p>
		<p>Contenu de la table <code>University</code> et alias. Lorsque
		plusieurs lignes partagent le même identifiant, seul la première est
		enregistrée dans la base de données. Les autres sont utilisés pour
		corriger les noms présents dans les données brutes.</p>
	</dd>
</dl>

# CSV
All the CSV files are RFC 4180 files, without header. /
Tous les fichiers CSV sont des fichiers RFC 4180, sans l’en-tête.

# License / Licence
## Data and Web Pages / Données et pages web
© 2002-2016 CS Games | All Rights Reserved / Tous droits réservés

## All the Remaining / Tous le reste
Copyright (c) 2016, jcbrinfo <jcbrinfo@users.noreply.github.com>.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

© jcbrinfo <jcbrinfo@users.noreply.github.com>, 2016.

Il est autorisé d’utiliser, de reproduire, de modifier et/ou de distribuer
cette œuvre, avec ou sans frais, à condition que la mention de droit d’auteur
ainsi que le présent paragraphe apparaissent dans toutes les reproductions.
