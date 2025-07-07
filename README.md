# AI Web App

A full-stack AI web application built with Next.js, FastAPI, Supabase, and LiteLLM. This template provides a solid foundation for building production-ready AI applications.

## Tech Stack

- **Frontend**: Next.js 15 with TypeScript and Tailwind CSS
- **Backend**: FastAPI with Python 3.11
- **Database**: Supabase (PostgreSQL)
- **LLM Access**: LiteLLM (supports OpenAI, Anthropic, and more)
- **Deployment**: Fly.io

## Features

- 🤖 Multi-model AI chat interface
- 🔐 User authentication with Supabase
- 💬 Conversation history and management
- 🎯 Custom AI agents with configurable prompts
- 📊 Token usage tracking
- 🚀 Production-ready deployment configuration

## Project Structure

```
ai-web-app/
├── frontend/              # Next.js frontend
│   ├── src/
│   │   ├── app/          # App Router pages
│   │   ├── components/   # React components
│   │   └── lib/          # Utilities and API clients
│   ├── Dockerfile
│   └── fly.toml
├── backend/              # FastAPI backend
│   ├── routers/          # API routes
│   ├── database/         # Database configuration
│   ├── models/           # Pydantic models
│   ├── utils/            # Utilities
│   ├── main.py           # FastAPI app
│   ├── requirements.txt
│   ├── Dockerfile
│   └── fly.toml
└── README.md
```

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Supabase account
- LLM API keys (OpenAI, Anthropic, etc.)

### 1. Clone and Setup

```bash
git clone <your-repo>
cd ai-web-app
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Edit .env with your keys
# SUPABASE_URL=your_supabase_url
# SUPABASE_KEY=your_supabase_anon_key
# OPENAI_API_KEY=your_openai_api_key
# ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 3. Database Setup

1. Create a new Supabase project
2. Run the SQL schema in `backend/database/schemas.sql`
3. Configure your environment variables

### 4. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.local.example .env.local

# Edit .env.local with your Supabase keys
# NEXT_PUBLIC_API_URL=http://localhost:8000
# NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
# NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### 5. Run Development Servers

**Backend:**
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run dev
```

Visit `http://localhost:3000` to see your application!

## Deployment

### Fly.io Deployment

1. Install Fly CLI: `https://fly.io/docs/getting-started/installing-flyctl/`
2. Login: `flyctl auth login`

**Deploy Backend:**
```bash
cd backend
flyctl launch --no-deploy
flyctl secrets set SUPABASE_URL=your_url SUPABASE_KEY=your_key OPENAI_API_KEY=your_key
flyctl deploy
```

**Deploy Frontend:**
```bash
cd frontend
flyctl launch --no-deploy
flyctl secrets set NEXT_PUBLIC_API_URL=your_backend_url NEXT_PUBLIC_SUPABASE_URL=your_url
flyctl deploy
```

## API Endpoints

### Health
- `GET /health` - Health check

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user

### AI
- `POST /ai/chat` - Chat completion
- `GET /ai/models` - Get available models

## Environment Variables

### Backend (.env)
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
JWT_SECRET=your_jwt_secret
ENVIRONMENT=development
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

## Development

### Adding New Models

Add new models to the `get_available_models()` function in `backend/utils/ai_client.py` and update the frontend model selector.

### Adding New API Endpoints

1. Create router in `backend/routers/`
2. Add to `main.py` with `app.include_router()`
3. Update frontend API client in `frontend/src/lib/api.ts`

### Database Schema Changes

1. Update `backend/database/schemas.sql`
2. Run migrations in Supabase dashboard
3. Update Pydantic models if needed

## Security

- Row Level Security (RLS) enabled on all tables
- API key rotation supported
- CORS configured for frontend domain
- Environment variables for sensitive data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see LICENSE file for details