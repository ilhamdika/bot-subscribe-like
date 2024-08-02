# Otomatisasi YouTube dengan Selenium

Skrip ini mengotomatisasi proses login ke YouTube menggunakan akun Google dan melakukan berbagai tindakan pada halaman video, seperti memberi like pada video, berlangganan channel, dan melompati iklan.

## Prasyarat

* Python 3.x
* Selenium
* undetected_chromedriver (opsional)

## Instalasi

1. Instal dependensi yang diperlukan:

<pre><div class="my-2 language-shell relative mt-6 border-[1px] border-gray-700" aria-label="highlighted-code-my-2 language-shell"><div class="absolute right-2 top-0 z-50 flex w-min -translate-y-3/4 flex-row space-x-1 rounded border border-gray-500/30 bg-editor-content-area"><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-white hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-white hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert in Terminal</button></div><div class="w-full overflow-x-auto"><div><code class="language-shell"><span>pip </span><span class="token">install</span><span> selenium undetected_chromedriver</span></code></div></div></div></pre>

2. Unduh eksekusi ChromeDriver yang sesuai dengan sistem operasi Anda dari situs resmi: `<a href="https://developer.chrome.com/docs/chromedriver/downloads">Unduh</a>`
3. Tempatkan eksekusi ChromeDriver di PATH sistem Anda atau tentukan jalur di dalam kode.

## Penggunaan

1. Buat file JSON bernama `data.json` dengan struktur sebagai berikut:

<pre><div class="my-2 language-json relative mt-6 border-[1px] border-gray-700" aria-label="highlighted-code-my-2 language-json"><div class="absolute right-2 top-0 z-50 flex w-min -translate-y-3/4 flex-row space-x-1 rounded border border-gray-500/30 bg-editor-content-area"><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-white hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-white hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert</button></div><div class="w-full overflow-x-auto"><div><code class="language-json"><span class="token">[</span><span>
</span><span></span><span class="token">{</span><span>
</span><span></span><span class="token">"email"</span><span class="token">:</span><span></span><span class="token">"your_email@example.com"</span><span class="token">,</span><span>
</span><span></span><span class="token">"password"</span><span class="token">:</span><span></span><span class="token">"your_password"</span><span>
</span><span></span><span class="token">}</span><span class="token">,</span><span>
</span><span></span><span class="token">{</span><span>
</span><span></span><span class="token">"email"</span><span class="token">:</span><span></span><span class="token">"another_email@example.com"</span><span class="token">,</span><span>
</span><span></span><span class="token">"password"</span><span class="token">:</span><span></span><span class="token">"another_password"</span><span>
</span><span></span><span class="token">}</span><span>
</span><span></span><span class="token">]</span></code></div></div></div></pre>

2. Buat file JSON lain bernama `data_url.json` dengan struktur sebagai berikut:

<pre><div class="my-2 language-json relative mt-6 border-[1px] border-gray-700" aria-label="highlighted-code-my-2 language-json"><div class="absolute right-2 top-0 z-50 flex w-min -translate-y-3/4 flex-row space-x-1 rounded border border-gray-500/30 bg-editor-content-area"><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-white hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-white hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert</button></div><div class="w-full overflow-x-auto"><div><code class="language-json"><span class="token">[</span><span>
</span><span></span><span class="token">{</span><span>
</span><span></span><span class="token">"url"</span><span class="token">:</span><span></span><span class="token">"https://www.youtube.com/watch?v=VIDEO_ID"</span><span>
</span><span></span><span class="token">}</span><span class="token">,</span><span>
</span><span></span><span class="token">{</span><span>
</span><span></span><span class="token">"url"</span><span class="token">:</span><span></span><span class="token">"https://www.youtube.com/watch?v=ANOTHER_VIDEO_ID"</span><span>
</span><span></span><span class="token">}</span><span>
</span><span></span><span class="token">]</span></code></div></div></div></pre>

3. Jalankan skrip:

<pre><div class="my-2 language-shell relative mt-6 border-[1px] border-gray-700" aria-label="highlighted-code-my-2 language-shell"><div class="absolute right-2 top-0 z-50 flex w-min -translate-y-3/4 flex-row space-x-1 rounded border border-gray-500/30 bg-editor-content-area"><button data-tooltip="Copied!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-white hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Copy</button><button data-tooltip="Inserted!" class="relative z-10 rounded px-2 py-1 text-xs whitespace-nowrap text-white hover:bg-gray-500/10 cursor-pointer disabled:cursor-not-allowed after:absolute after:-bottom-1 after:left-2/4 after:-translate-x-1/2 after:translate-y-full after:rounded after:bg-black after:px-1 after:py-0.5 after:text-xs after:text-white after:opacity-0 transition-opacity after:duration-200 after:content-[attr(data-tooltip)]">Insert in Terminal</button></div><div class="w-full overflow-x-auto"><div><code class="language-shell"><span>python youtube.py</span></code></div></div></div></pre>

Skrip akan login ke YouTube menggunakan akun yang diberikan dan melakukan tindakan yang ditentukan pada setiap URL video.

## Dependensi

* json
* undetected_chromedriver (opsional)
* selenium
* time
