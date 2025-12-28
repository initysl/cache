'use client';

import Link from 'next/link';
import { LinkIcon, MoreHorizontal } from 'lucide-react';

export default function FileCard() {
  return (
    <div className='w-full rounded-2xl bg-white p-4 shadow-sm border border-gray-100'>
      {/* Header */}
      <div className='flex items-center justify-between'>
        {/* Left */}
        <div className='flex items-center gap-3'>
          {/* Icon */}
          <div className='flex h-9 w-9 items-center justify-center rounded-xl bg-gray-100/80 ring-1 ring-gray-200'>
            <LinkIcon size={18} className='text-gray-700' />
          </div>

          {/* Text */}
          <div className='leading-tight'>
            <p className='text-sm font-medium text-gray-900'>Quick action</p>
          </div>
        </div>

        {/* Menu */}
        <button
          aria-label='More options'
          className='rounded-lg p-1.5 text-gray-500 hover:bg-gray-100 hover:text-gray-700 transition-colors
    '
        >
          <MoreHorizontal size={16} />
        </button>
      </div>

      {/* Footer */}
      <div className='flex flex-col gap-2 mt-5 rounded-xl border border-gray-200 bg-gray-50 px-3 py-2 text-center'>
        <Link
          href='/dashboard/documents'
          className='text-xs text-gray-500 hover:text-gray-900 bg-white p-5 rounded-2xl transition-colors'
        >
          Documents
        </Link>

        <Link
          href='/dashboard/settings'
          className='text-xs text-gray-500 hover:text-gray-900 bg-gray-200 p-5 rounded-2xl transition-colors'
        >
          Settings
        </Link>
      </div>
    </div>
  );
}
