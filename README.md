# Expense Splitter

> Split group expenses and settle up with the fewest payments.

Hack Day Haldia x GRID community - 6-hour build challenge

**Repo:** `team-vortex` | **Stack:** Python / Flask | **Difficulty:** Medium-Hard | **Time:** 6 hours

## Brief
Friends share trips, flats and events. Build a tracker that records who paid what and tells everyone exactly who should pay whom.

## Core tasks (must-do)
- [ ] Groups with members; add expenses (payer, amount, description, date, who shares it)
- [ ] Equal, exact-amount and percentage splits, validated so the shares add up
- [ ] Net balance per member
- [ ] Minimum set of settle-up payments (match debtors with creditors)
- [ ] Edit / delete expenses and mark a settlement as paid; balances update
- [ ] Persist everything in SQLite (helper already in app.py)
- [ ] UI: group page with members, expense form and history, balances table, settlement list

## Bonus tasks (only after the core works)
- [ ] UPI payment link and QR for each settlement
- [ ] Category-wise spending chart and monthly summary
- [ ] Add an expense from free text ('Dinner 1200 paid by Ravi, split with Sam and Ana') using an AI model
- [ ] Multi-currency with a fixed rates table

## What is already here
- `index.html` - base page that pings `/api/health`
- `app.py` - Flask app with a SQLite helper (`db()`, `init_db()`), `/api/health` and TODO endpoint stubs (they return 501 until you implement them)
- `requirements.txt` - `flask`, `gunicorn`

## Run locally
```bash
pip install -r requirements.txt
python app.py   # then open http://127.0.0.1:5000
```

## Deploy
Any Python host works (for example Render or PythonAnywhere). Start command: `gunicorn app:app`. Free hosts may reset the filesystem on restart, so the SQLite file can reset - fine for a demo.

## Suggested pacing
- Hour 1: read this README, agree on a plan and split the work
- Hours 2-4: build the core tasks
- Hour 5: integrate, polish, then bonus tasks if time allows
- Hour 6: deploy, open the Pull Request, submit on the MLH platform (OrganizerHQ)

## Submission checklist
- [ ] All core tasks work end to end
- [ ] Project is deployed and the live link opens
- [ ] Pull Request created on the Voyage GitHub repository assigned to your team
- [ ] Project submitted on the MLH platform (OrganizerHQ) - instructions are shared at the start of the event

## Rules
- Build new features on top of this starter project and integrate them.
- Teams of 3-4; every member must be present.
- AI tools and open-source / open-weight models are fully allowed.
