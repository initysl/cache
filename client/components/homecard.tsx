import { motion } from 'framer-motion';

export default function HomeCard() {
  return (
    <div className='flex items-center justify-center w-full py-24 px-4'>
      <div className='relative w-full max-w-5xl flex items-center justify-center min-h-[400px]'>
        {/* Left Card */}
        <motion.div
          initial={{ opacity: 0, x: -100, rotateY: -15 }}
          animate={{ opacity: 1, x: 0, rotateY: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className='absolute left-1/2 -translate-x-[140%] top-1/2 -translate-y-1/2 w-[220px] h-[340px] rounded-3xl border border-orange-500 shadow-xl scale-95 z-0 flex-shrink-0 bg-orange-600 '
        />

        {/* Center Card (Main) */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className='absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[260px] h-[400px] rounded-3xl border border-blue-500 shadow-2xl z-10 flex-shrink bg-transparent'
        />

        {/* Right Card */}
        <motion.div
          initial={{ opacity: 0, x: 100, rotateY: 15 }}
          animate={{ opacity: 1, x: 0, rotateY: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className='absolute left-1/2 translate-x-[40%] top-1/2 -translate-y-1/2 w-[220px] h-[340px] rounded-3xl border border-orange-500 shadow-xl scale-95 z-0 flex-shrink-0 bg-zinc-500'
        />
      </div>
    </div>
  );
}
