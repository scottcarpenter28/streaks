
import Image from "next/image";

export default function Home() {
  return (
    <main>
      <div className='scheme-dark'>
        <div className='mx-auto max-7-l px-4 py-24 sm:px-6 sm:py-32 lg:px-8'>
          <div className='mx-auto max-w-2xl bg-zinc-800 p-10'>
            <form>
              <div className='space-y-12'>
                <div className='border-b border-white/10 pb-12'>
                  <h1 className="font-mono text-8xl text-center">Streaks</h1>
                  <p className="font-mono text-center text-lg">A "dont break the chain" habit tracker</p>
                  <div className="mt-10 grid grid-cols-1 sm:grid-cols-6">
                    <div className='sm:col-span-4'>
                      <label htmlFor='username' className='block text-sm/6 font-medium text-white'>Username</label>
                      <div className='mt-2'>
                        <div className='flex items-center rounded-md bg-white/5 pl-3 outline-1 -outline-offset-1 outline-white/10 focus-within:outline-2 focus-within:-outline-2 focus-within:outline-indigo-500'>
                          <input id='username' name='username' type='text' className='block min-w-0 grow bg-transparent py-1.5 pr-3 pl-1 text-base text-white focus:outline-none sm:text-sm/6'/>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className="mt-10 grid grid-cols-1 sm:grid-cols-6">
                    <div className='sm:col-span-4'>
                      <label htmlFor='username' className='block text-sm/6 font-medium text-white'>Password</label>
                      <div className='mt-2'>
                        <div className='flex items-center rounded-md bg-white/5 pl-3 outline-1 -outline-offset-1 outline-white/10 focus-within:outline-2 focus-within:-outline-2 focus-within:outline-indigo-500'>
                          <input id='username' name='username' type='password' className='block min-w-0 grow bg-transparent py-1.5 pr-3 pl-1 text-base text-white focus:outline-none sm:text-sm/6'/>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </main>
  );
}
