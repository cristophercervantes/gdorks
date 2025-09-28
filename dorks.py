#!/usr/bin/env python3
]


window = sg.Window('Dorker — presets', layout, finalize=True)


while True:
event, values = window.read()
if event in (sg.WIN_CLOSED, 'Exit'):
break
if event == 'Clear':
window['-OUTPUT-'].update('')
continue
if event == 'Load Preset':
cat = values['-CAT-']
if not cat:
sg.popup('Choose a preset category first')
continue
# show first query in output
q = presets.get(cat, [])
window['-OUTPUT-'].update('\n\n'.join(q) if q else 'No queries')
if event == 'Open Selected Query':
q = values['-DORK-'].strip()
if not q:
cat = values['-CAT-']
if not cat:
sg.popup('Select a preset or paste a dork')
continue
# use first query of category
q = presets.get(cat, [''])[0]
pages = int(values['-PAGES-'] or 1)
paginate = values['-PAG-']
opened = 0
for p in range(pages):
start = p*10 if paginate else 0
url = build_google_search_url(q, start)
webbrowser.open_new_tab(url)
opened += 1
window['-OUTPUT-'].update(f'Opened {opened} tab(s) for query:\n{q}')
if event == 'Open All Queries':
cat = values['-CAT-']
if not cat:
sg.popup('Select a preset category to open all queries')
continue
qlist = presets.get(cat, [])
pages = int(values['-PAGES-'] or 1)
paginate = values['-PAG-']
count = 0
for q in qlist:
for p in range(pages):
start = p*10 if paginate else 0
url = build_google_search_url(q, start)
webbrowser.open_new_tab(url)
count += 1
window['-OUTPUT-'].update(f'Opened {count} tabs for category {cat}')


window.close()
