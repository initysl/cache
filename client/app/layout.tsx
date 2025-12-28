import type { Metadata } from 'next';
import {
  Geist,
  Geist_Mono,
  Exo_2,
  Cherry_Swash,
  Sedgwick_Ave_Display,
} from 'next/font/google';
import './globals.css';
import { Providers } from '@/components/providers';

const geistSans = Geist({
  variable: '--font-geist-sans',
  subsets: ['latin'],
});

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
});

const exo2 = Exo_2({
  variable: '--font-exo-2',
  subsets: ['latin'],
});

const cherry = Cherry_Swash({
  variable: '--font-cherry-swash',
  weight: '400',
  subsets: ['latin'],
});

const sedgwick = Sedgwick_Ave_Display({
  variable: '--font-sedgwick-ave-display',
  weight: '400',
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: 'Vectorsnap',
  description: 'A knowledge base service',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang='en'>
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${cherry.variable} ${sedgwick.variable} ${exo2.variable} antialiased`}
      >
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
