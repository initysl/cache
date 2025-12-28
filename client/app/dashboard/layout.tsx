import Profile from '@/components/dashboard/Profile';
import Promptbar from '@/components/dashboard/Promptbar';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className='flex flex-col items-center justify-center'>
      <div>
        <Profile />
      </div>
      <main className='w-full max-w-5xl h-[calc(95vh-6rem)] overflow-y-auto p-5 mt-5 rounded-2xl'>
        {children}
      </main>
      <div>
        <Promptbar />
      </div>
    </div>
  );
}
