import ChatInterface from '@/components/ChatInterface'

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            <div className="flex items-center">
              <h1 className="text-2xl font-bold text-gray-900">AI Web App</h1>
            </div>
            <nav className="flex space-x-8">
              <a href="#" className="text-gray-500 hover:text-gray-900">Chat</a>
              <a href="#" className="text-gray-500 hover:text-gray-900">Agents</a>
              <a href="#" className="text-gray-500 hover:text-gray-900">Settings</a>
            </nav>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <div className="bg-white rounded-lg shadow h-[calc(100vh-200px)]">
            <ChatInterface />
          </div>
        </div>
      </main>
    </div>
  );
}
