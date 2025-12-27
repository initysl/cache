'use client';

import { useState } from 'react';
import { usePathname } from 'next/navigation';
import Link from 'next/link';
import {
  Home,
  Upload,
  FileText,
  Settings,
  ChevronDown,
  Menu,
  X,
} from 'lucide-react';
import { TbHexagonLetterV } from 'react-icons/tb';

export default function Navbar() {
  const pathname = usePathname();

  const [showUserMenu, setShowUserMenu] = useState(false);
  const [showMobileMenu, setShowMobileMenu] = useState(false);

  const navItems = [
    { name: 'Home', href: '/dashboard', icon: Home },
    { name: 'Upload', href: '/dashboard/upload', icon: Upload },
    { name: 'Documents', href: '/dashboard/documents', icon: FileText },
    { name: 'Settings', href: '/dashboard/settings', icon: Settings },
  ];

  return (
    <nav className='sticky top-0 z-50 exo'>
      <div className='max-w-7xl'>
        <div className='flex items-center justify-between h-16'>
          {/* Logo */}
          <Link href='/home' className='flex items-center gap-2'>
            <div className='w-10 h-10 bg-linear-to-br from-blue-600 to-purple-600 rounded-xl flex items-center justify-center'>
              <TbHexagonLetterV size={30} className='text-white' />
            </div>
          </Link>

          {/* Desktop Navigation */}
          <div className='hidden lg:flex items-center gap-2'>
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = pathname === item.href;

              return (
                <Link
                  key={item.name}
                  href={item.href}
                  className={`
                    flex items-center gap-2 px-4 py-2 rounded-full font-medium text-sm transition-all
                    ${
                      isActive
                        ? 'bg-gray-900 text-white shadow-md'
                        : 'text-gray-600 bg-gray-200 hover:bg-gray-100 hover:text-gray-900'
                    }
                  `}
                >
                  <Icon className='w-4 h-4' />
                  <span>{item.name}</span>
                </Link>
              );
            })}
          </div>

          {/* Right Section */}
          <div className='flex items-center gap-2 sm:gap-4'>
            {/* User Menu - Desktop */}
            <div className='relative hidden sm:block'>
              <button
                onClick={() => setShowUserMenu((v) => !v)}
                className='flex items-center gap-2 p-2 hover:bg-gray-100 rounded-lg transition-colors'
              >
                <img
                  src='https://api.dicebear.com/7.x/avataaars/svg?seed=Jessica'
                  alt='User'
                  className='w-8 h-8 rounded-full'
                />
                <div className='text-left hidden md:block'>
                  <p className='text-sm font-semibold text-gray-900'>Jessica</p>
                  <p className='text-xs text-gray-500'>jessica@email.com</p>
                </div>
                <ChevronDown className='w-4 h-4 text-gray-500 hidden md:block' />
              </button>

              {showUserMenu && (
                <div className='absolute right-0 mt-2 w-56 bg-white rounded-xl shadow-lg border border-gray-200 py-2 z-50'>
                  <div className='px-4 py-3 border-b border-gray-100'>
                    <p className='text-sm font-semibold text-gray-900'>
                      Jessica Parker
                    </p>
                    <p className='text-xs text-gray-500'>jessica@email.com</p>
                  </div>

                  <Link
                    href='/settings/profile'
                    className='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100'
                  >
                    Profile Settings
                  </Link>
                  <Link
                    href='/settings/api-keys'
                    className='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100'
                  >
                    API Keys
                  </Link>
                  <Link
                    href='/billing'
                    className='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100'
                  >
                    Billing
                  </Link>

                  <div className='border-t border-gray-100 mt-2 pt-2'>
                    <button className='w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50'>
                      Sign Out
                    </button>
                  </div>
                </div>
              )}
            </div>

            {/* Mobile Menu Button */}
            <button
              onClick={() => setShowMobileMenu((v) => !v)}
              className='lg:hidden p-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors'
            >
              {showMobileMenu ? (
                <X className='w-6 h-6' />
              ) : (
                <Menu className='w-6 h-6' />
              )}
            </button>
          </div>
        </div>

        {/* Mobile Menu */}
        {showMobileMenu && (
          <div className='lg:hidden py-4 border-t border-gray-200'>
            <div className='space-y-2 mb-4'>
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = pathname === item.href;

                return (
                  <Link
                    key={item.name}
                    href={item.href}
                    onClick={() => setShowMobileMenu(false)}
                    className={`
                      w-full flex items-center gap-3 px-4 py-3 rounded-lg font-medium text-sm transition-all
                      ${
                        isActive
                          ? 'bg-gray-900 text-white'
                          : 'text-gray-600 hover:bg-gray-100'
                      }
                    `}
                  >
                    <Icon className='w-5 h-5' />
                    <span>{item.name}</span>
                  </Link>
                );
              })}
            </div>

            {/* Mobile User Section */}
            <div className='sm:hidden border-t border-gray-200 pt-4'>
              <div className='flex items-center gap-3 px-4 py-2 mb-2'>
                <img
                  src='https://api.dicebear.com/7.x/avataaars/svg?seed=Jessica'
                  alt='User'
                  className='w-10 h-10 rounded-full'
                />
                <div>
                  <p className='text-sm font-semibold text-gray-900'>
                    Jessica Parker
                  </p>
                  <p className='text-xs text-gray-500'>jessica@email.com</p>
                </div>
              </div>

              <div className='space-y-1 px-2'>
                <Link
                  href='/settings/profile'
                  className='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded-lg'
                >
                  Profile Settings
                </Link>
                <Link
                  href='/settings/api-keys'
                  className='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded-lg'
                >
                  API Keys
                </Link>
                <Link
                  href='/billing'
                  className='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded-lg'
                >
                  Billing
                </Link>
                <button className='w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 rounded-lg'>
                  Sign Out
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}
