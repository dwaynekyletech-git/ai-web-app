### 🔄 Project Awareness & Context
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `TASK.md`** before starting a new task. If the task isn’t listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.
- **This is a full-stack AI web application** with Next.js frontend, FastAPI backend, Supabase database, and LiteLLM for AI model access.
- **Check `backend/main.py`** to understand the API structure and available routers (auth, ai, health, agents).
- **Use the virtual environment** (`backend/venv/`) whenever executing Python commands or running the backend.

### 🏗️ Architecture & Tech Stack
- **Frontend**: Next.js 15 with TypeScript, React, Tailwind CSS, and Supabase client
- **Backend**: FastAPI with Python 3.11, Pydantic models, JWT authentication
- **Database**: Supabase (PostgreSQL) with Row Level Security (RLS)
- **AI Integration**: LiteLLM supporting OpenAI, Anthropic, and other model providers
- **Deployment**: Fly.io with Docker containers for both frontend and backend

### 🧱 Code Structure & Modularity
- **Backend Structure**:
  - `main.py` - FastAPI app with CORS and router configuration
  - `routers/` - API endpoints organized by feature (auth, ai, health, agents)
  - `database/` - Supabase client configuration and schemas
  - `models/` - Pydantic models for request/response validation
  - `utils/` - Shared utilities including AI client wrapper
- **Frontend Structure**:
  - `src/app/` - Next.js App Router pages
  - `src/components/` - React components (ChatInterface, etc.)
  - `src/lib/` - API client and Supabase configuration
- **Never create files longer than 500 lines** - split into logical modules
- **Use TypeScript** for all frontend code with proper type definitions
- **Follow FastAPI patterns** with Pydantic models and dependency injection

### 🤖 AI Integration Patterns
- **Use LiteLLM** for model access - supports OpenAI, Anthropic, and other providers
- **All AI requests** should go through `routers/ai.py` endpoints
- **Model configuration** should be centralized in the AI router
- **Always validate** AI requests with Pydantic models (`ChatRequest`, `ChatResponse`)
- **Handle AI errors gracefully** with appropriate HTTP status codes
- **Track token usage** when available from the model provider

### 🔐 Authentication & Security
- **Use Supabase Auth** for user authentication with JWT tokens
- **All protected routes** should verify JWT tokens
- **Enable Row Level Security (RLS)** on all database tables
- **Never expose service role keys** in frontend code
- **Use environment variables** for all sensitive configuration

### 📊 Database Patterns
- **Use Supabase client** from `database/supabase.py`
- **Separate clients** for user operations (`supabase`) and admin operations (`admin_supabase`)
- **Update `database/schemas.sql`** for any schema changes
- **Use Pydantic models** for data validation and serialization
- **Always use RLS policies** for data access control

### 🎨 Frontend Development
- **Use Tailwind CSS** for styling with responsive design
- **TypeScript is required** for all React components
- **API calls** should go through `lib/api.ts` client
- **State management** with React hooks (useState, useEffect, useRef)
- **Real-time updates** can use Supabase subscriptions
- **Form handling** should include proper validation and error states
### ✅ Task Completion
- **Mark completed tasks in `TASK.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a “Discovered During Work” section.

### 🧪 Testing & Reliability
- **Create unit tests** for all backend endpoints using pytest
- **Test AI integrations** with mocked responses to avoid API costs
- **Frontend tests** should cover component rendering and user interactions
- **Test authentication flows** including token validation
- **Database tests** should use separate test database or mocked client

### 🚀 Development & Deployment
- **Backend development**: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
- **Frontend development**: `npm run dev` (uses Next.js with Turbopack)
- **Environment variables** are required for both frontend and backend
- **Docker containers** are configured for production deployment
- **Fly.io deployment** uses `fly.toml` configuration files


### 📚 Documentation & API Design
- **Follow OpenAPI standards** with FastAPI automatic documentation
- **Use Pydantic models** for request/response documentation
- **Update README.md** when adding new features or changing setup
- **Document API endpoints** with clear descriptions and examples
- **Include error handling** in all API responses

### 💡 Best Practices
- **CORS configuration** allows frontend at `http://localhost:3000`
- **Use relative imports** within backend packages
- **Load environment variables** with `python-dotenv` and `load_dotenv()`
- **Async/await patterns** for all FastAPI endpoints
- **Proper error handling** with FastAPI HTTPException
- **Rate limiting** should be considered for AI endpoints
- **Logging** should be implemented for debugging and monitoring

### 🔧 Specific File Patterns
- **Backend routers** should follow the pattern in `routers/ai.py`
- **Frontend components** should follow the pattern in `components/ChatInterface.tsx`
- **Database clients** should use the factory functions in `database/supabase.py`
- **API requests** should use the axios client from `lib/api.ts`
- **Environment variables** should be loaded and validated at startup

### 🧠 AI Development Guidelines
- **Never hardcode API keys** - always use environment variables
- **Support multiple models** through LiteLLM configuration
- **Implement proper error handling** for AI API failures
- **Consider token limits** and implement streaming for long responses
- **Cache responses** when appropriate to reduce API costs
- **Monitor usage** and implement rate limiting for production

### 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified Python packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.