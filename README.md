# RasoiMate — Backend (V1 MVP) 🥘

RasoiMate is a decision engine that answers "What should I cook today?" for Indian households using a swipe-style interface.

This repository contains the FastAPI backend, database models, and the V1 recommendation engine.

**Quick links**
- **API docs:** http://localhost:8000/docs (after starting the app)
- **Health check:** http://localhost:8000/

---

**Core Features (MVP)**

- **Daily Decision Deck:** Curated stack of 5–7 recipe cards tailored to user inventory and time of day.
- **Inventory-first:** Prioritizes recipes that match ingredients in the user's pantry.
- **Rule-based recommendation:** Heuristic engine for V1 combining inventory overlap, freshness, and effort.
- **Fast API:** Built with FastAPI and async SQLAlchemy for responsive endpoints.

---

**Tech Stack**

- **Python:** 3.9+
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (async)
- **Containerization:** Docker + Docker Compose
- **Cache (future):** Redis

---

**Project layout**

```text
rasoimate-backend/
├── app/
│   ├── api/v1.py          # API routes
│   ├── core/config.py     # configuration and env
│   ├── db/models.py       # SQLAlchemy models
│   ├── services/engine.py # recommendation logic
│   └── main.py            # FastAPI app entry
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

---

**Quick start (docker)**

You only need Docker and Docker Compose to run the stack locally.

1. Build and start the services:

```bash
docker compose up --build
```

2. When logs show "Application startup complete":

- Open Swagger UI: http://localhost:8000/docs
- Health check: http://localhost:8000/

---

**API (example endpoints)**

- Get daily deck

  - Method: `GET`
  - Path: `/api/v1/deck`
  - Description: Returns the curated card stack for the user.

  Example curl:

  ```bash
  curl http://localhost:8000/api/v1/deck
  ```

- Record swipe

  - Method: `POST`
  - Path: `/api/v1/swipe`
  - Payload (JSON):

    ```json
    {
      "recipe_id": 101,
      "action": "RIGHT"
    }
    ```

---

**Recommendation engine (V1)**

The V1 engine is a weighted heuristic located at `app/services/engine.py`.

The score used to rank recipes (KaTeX formula):

$$
	ext{Score} = (\text{InventoryMatch} \times 20) + (\text{FreshnessBonus} \times 15) - (\text{Effort} \times 5)
$$

- InventoryMatch: set overlap between recipe ingredients and user inventory (high weight).
- FreshnessBonus: prefers recipes using soon-to-expire items.
- Effort: penalizes high-effort recipes during busy times.

**Behavior notes**

- Dietary filters are applied as hard constraints (e.g., vegetarian users won't see non-veg recipes).

---

**Roadmap (selected)**

- V2: Collaborative filtering / ML-based recommendations
- V1.1: Redis caching to precompute decks
- UX: Inventory scanner (OCR) to add ingredients quickly

---

**License**

Private — RasoiMate Inc.

---

**Commit example**

```bash
git add README.md
git commit -m "Improve README: clearer structure and usage"
git push
```