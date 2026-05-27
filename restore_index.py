import re

content = """1: <!DOCTYPE html>
2: <html lang="ko">
3:   <head>
4:     <meta charset="UTF-8" />
5:     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
6:     <title>NURA | 전국대학교로켓연합회</title>
7:     <meta name="description" content="전국대학교로켓연합회(NURA)는 국내 대학 간 로켓 학술 교류와 발사대회를 통해 대한민국 우주 · 항공 · 방산 인재를 연결하고 성장시키는 연합회입니다." />
8:     <meta property="og:title" content="NURA | 전국대학교로켓연합회" />
9:     <meta property="og:description" content="전국대학교로켓연합회(NURA)는 국내 대학 간 로켓 학술 교류와 발사대회를 통해 대한민국 우주 · 항공 · 방산 인재를 연결하고 성장시키는 연합회입니다." />
10:     <meta property="og:type" content="website" />
11:     <meta property="og:url" content="https://nura.kr/" />
12:     <meta property="og:image" content="https://nura.kr/source/resources/og-image.jpg" />
13:     <meta property="og:image:secure_url" content="https://nura.kr/source/resources/og-image.jpg" />
14:     <meta property="og:image:width" content="1200" />
15:     <meta property="og:image:height" content="630" />
16:     <meta property="og:image:alt" content="NURA 로고" />
17:     <meta name="twitter:card" content="summary_large_image" />
18:     <meta name="twitter:image" content="https://nura.kr/source/resources/og-image.jpg" />
19:     <link rel="icon" type="image/png" sizes="32x32" href="source/resources/favicon-32x32.png" />
20:     <link rel="icon" type="image/png" sizes="16x16" href="source/resources/favicon-16x16.png" />
21:     <link rel="shortcut icon" type="image/png" href="source/resources/favicon-32x32.png" />
22:     <link rel="apple-touch-icon" href="source/resources/nura-icon.png" />
23:     <meta name="apple-mobile-web-app-capable" content="yes" />
24:     <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
25:     <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin />
26:     <script src="https://cdn.tailwindcss.com"></script>
27:     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
28:     <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
29:     <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css" />
30: 
31:     <style>
32:       html { scroll-behavior: smooth; }
33:       html, body { background-color: #030712; overflow-x: hidden; }
34:       body { font-family: 'Pretendard', system-ui, -apple-system, BlinkMacSystemFont, sans-serif; }
35:       .page-shell { min-height: 100vh; }
36: 
37:       .hero-title {
38:         font-size: 88px;
39:         line-height: 1.15;
40:       }
41: 
42:       .hero-subtitle {
43:         margin-top: 8px;
44:         font-size: 28px;
45:         line-height: 1.45;
46:       }
47: 
48:       .reveal-line {
49:         display: block;
50:         overflow: hidden;
51:       }
52: 
53:       .reveal-text {
54:         display: inline-block;
55:         transform: translateY(108%);
56:         will-change: transform;
57:       }
58: 
59:       .reveal-line.is-visible .reveal-text {
60:         animation: textRise 0.95s cubic-bezier(0.22, 1, 0.36, 1) forwards;
61:       }
62: 
63:       @keyframes textRise {
64:         from {
65:           transform: translateY(108%);
66:         }
67:         to {
68:           transform: translateY(0);
69:         }
70:       }
71: 
72:       .hero-copy-block {
73:         width: fit-content;
74:         max-width: 100%;
75:       }
76: 
77:       .hero-content-wrap {
78:         align-items: flex-start;
79:       }
80: 
81:       .hero-progress-inline {
82:         margin-top: 18px;
83:         display: grid;
84:         grid-template-columns: auto 1fr;
85:         align-items: center;
86:         column-gap: 18px;
87:         width: 100%;
88:       }
89: 
90:       .hero-progress-toggle {
91:         flex: 0 0 auto;
92:         width: 36px;
93:         height: 28px;
94:         display: inline-flex;
95:         align-items: center;
96:         justify-content: center;
97:         gap: 7px;
98:         background: transparent;
99:         border: 0;
100:         padding: 0;
101:         cursor: pointer;
102:         appearance: none;
103:       }
104: 
105:       .hero-progress-toggle .pause-bar {
106:         display: block;
107:         width: 4px;
108:         height: 24px;
109:         border-radius: 999px;
110:         background: rgba(255, 255, 255, 0.96);
111:       }
112: 
113:       .hero-progress-toggle.is-play {
114:         gap: 0;
115:       }
116: 
117:       .hero-progress-toggle.is-play::before {
118:         content: "";
119:         display: block;
120:         width: 0;
121:         height: 0;
122:         border-top: 9px solid transparent;
123:         border-bottom: 9px solid transparent;
124:         border-left: 14px solid rgba(255, 255, 255, 0.96);
125:         margin-left: 2px;
126:       }
127: 
128:       .hero-progress-toggle.is-play .pause-bar {
129:         display: none;
130:       }
131: 
132:       .hero-progress-track {
133:         position: relative;
134:         height: 3px;
135:         width: 100%;
136:         background: rgba(255, 255, 255, 0.22);
137:         overflow: hidden;
138:       }
139: 
140:       .hero-progress-fill {
141:         position: absolute;
142:         left: 0;
143:         top: 0;
144:         bottom: 0;
145:         width: 0%;
146:         background: rgba(255, 255, 255, 0.95);
147:         transform-origin: left center;
148:       }
149: 
150:       @media (max-width: 767px) {
151:         #home {
152:           height: 100svh;
153:           min-height: 560px;
154:         }
155: 
156:         .hero-content-wrap {
157:           align-items: flex-end;
158:           padding-top: 0;
159:           padding-bottom: clamp(5rem, 14vh, 7rem);
160:         }
161: 
162:         .hero-title {
163:           font-size: clamp(1.7rem, 8vw, 2.45rem);
164:           line-height: 1.18;
165:         }
166: 
167:         .hero-subtitle {
168:           margin-top: 2vw;
169:           font-size: clamp(0.9rem, 3.7vw, 1.08rem);
170:           line-height: 1.35;
171:         }
172: 
173:         .hero-progress-inline {
174:           margin-top: 18px;
175:           column-gap: 14px;
176:         }
177: 
178:         .hero-progress-toggle {
179:           width: 24px;
180:           height: 20px;
181:           gap: 5px;
182:         }
183: 
184:         .hero-progress-toggle .pause-bar {
185:           width: 3px;
186:           height: 18px;
187:         }
188: 
189:         .hero-progress-toggle.is-play::before {
190:           border-top: 7px solid transparent;
191:           border-bottom: 7px solid transparent;
192:           border-left: 11px solid rgba(255, 255, 255, 0.96);
193:         }
194: 
195:         .hero-progress-track {
196:           height: 2px;
197:         }
198: 
199:         #sponsor-wall {
200:           padding: 0;
201:           grid-template-columns: repeat(2, minmax(0, 1fr));
202:           gap: 0.75rem;
203:         }
204: 
205:         #sponsor-wall > div {
206:           min-height: 88px;
207:           padding: 1rem;
208:           border-radius: 0.85rem;
209:         }
210: 
211:         #sponsor-wall img {
212:           max-height: 58px;
213:         }
214: 
215:         #nura-now > div,
216:         #nura-now + section > div,
217:         #nura-now + section + section > div {
218:           padding-top: 3rem;
219:           padding-bottom: 3rem;
220:         }
221:       }
222: 
223:       .news-card {
224:         display: flex;
225:         height: 100%;
226:         flex-direction: column;
227:       }
228: 
229:       .news-card__link {
230:         display: flex;
231:         height: 100%;
232:         flex-direction: column;
233:       }
234: 
235:       .news-card__body {
236:         display: flex;
237:         flex: 1;
238:         flex-direction: column;
239:       }
240: 
241:       .news-card__summary {
242:         margin-bottom: 1.5rem;
243:       }
244: 
245:       .news-card__cta {
246:         align-self: flex-start;
247:         margin-top: auto;
248:       }
249:     </style>
250: 
251:     <script src="./data/site-data.js?v=20260515"></script>
252:     <script src="./data/shared-layout.js?v=20260515" defer></script>
253:   </head>
254: 
255:   <body class="bg-black text-white min-h-screen overflow-x-hidden" data-current-page="home" data-base-path=".">
256:     <div class="page-shell flex flex-col">
257:       <div data-shared-header></div>
258: 
259:       <main class="w-full flex-1 flex flex-col">
260:         <section id="home" class="relative overflow-hidden flex flex-col justify-center h-screen w-full p-0 m-0">
261:           <div id="slideshow-bg" class="absolute inset-0 w-full h-full z-0 pointer-events-none">
262:             <img src="source/overview/blurred/slide1.webp" class="slide-img absolute inset-0 w-full h-full object-cover opacity-100 transition-opacity duration-[1500ms]" style="z-index:1;" alt="슬라이드1" fetchpriority="high" decoding="async">
263:             <img data-src="source/overview/blurred/slide2.webp" class="slide-img absolute inset-0 w-full h-full object-cover opacity-0 transition-opacity duration-[1500ms]" style="z-index:0;" alt="슬라이드2" decoding="async">
264:             <img data-src="source/overview/blurred/slide3.webp" class="slide-img absolute inset-0 w-full h-full object-cover opacity-0 transition-opacity duration-[1500ms]" style="z-index:0;" alt="슬라이드3" decoding="async">
265:             <img data-src="source/overview/blurred/slide4.webp" class="slide-img absolute inset-0 w-full h-full object-cover opacity-0 transition-opacity duration-[1500ms]" style="z-index:0;" alt="슬라이드4" decoding="async">
266:             <img data-src="source/overview/blurred/slide5.webp" class="slide-img absolute inset-0 w-full h-full object-cover opacity-0 transition-opacity duration-[1500ms]" style="z-index:0;" alt="슬라이드5" decoding="async">
267:             <img data-src="source/overview/blurred/slide6.webp" class="slide-img absolute inset-0 w-full h-full object-cover opacity-0 transition-opacity duration-[1500ms]" style="z-index:0;" alt="슬라이드6" decoding="async">
268:             <img data-src="source/overview/blurred/slide7.webp" class="slide-img absolute inset-0 w-full h-full object-cover opacity-0 transition-opacity duration-[1500ms]" style="z-index:0;" alt="슬라이드7" decoding="async">
269:             <img data-src="source/overview/blurred/slide8.webp" class="slide-img absolute inset-0 w-full h-full object-cover opacity-0 transition-opacity duration-[1500ms]" style="z-index:0;" alt="슬라이드8" decoding="async">
270:             <div class="absolute inset-0 bg-black/60 z-10"></div>
271:           </div>
272: 
273:           <div class="relative z-30 h-full w-full text-white">
274:             <div class="hero-content-wrap max-w-7xl mx-auto px-4 md:px-8 h-full flex pt-[450px] md:pt-[400px] lg:pt-[350px]">
275:               <div class="max-w-5xl flex flex-col items-start text-left">
276:                 <h1 class="hero-title text-white font-bold tracking-[-0.01em] break-keep hero-reveal">
277:                   <span class="reveal-line"><span class="reveal-text">함께 더 멀리</span></span>
278:                   <span class="reveal-line"><span class="reveal-text whitespace-nowrap">전국대학교로켓연합회</span></span>
279:                 </h1>
280: 
281:                 <div class="hero-copy-block">
282:                   <p class="hero-subtitle text-white font-medium hero-reveal">
283:                     <span class="reveal-line">
284:                       <span class="reveal-text">대한민국 미래 우주 · 항공 · 방산 인재들의 요람</span>
285:                     </span>
286:                   </p>
287: 
288:                   <div class="hero-progress-inline" aria-label="슬라이드 진행 상태">
289:                     <button class="hero-progress-toggle" type="button" aria-label="슬라이드 일시정지">
290:                       <span class="pause-bar"></span>
291:                       <span class="pause-bar"></span>
292:                     </button>
293: 
294:                     <div class="hero-progress-track">
295:                       <div class="hero-progress-fill"></div>
296:                     </div>
297:                   </div>
298:                 </div>
299:               </div>
300:             </div>
301:           </div>
302:         </section>
303: 
304:         <!-- NURA NOW -->
305:         <section id="nura-now" class="w-full bg-black border-t border-white/5">
306:           <div class="max-w-7xl mx-auto px-4 md:px-8 py-20">
307:             <div class="text-center mb-12">
308:               <h2 class="text-3xl md:text-4xl font-bold text-white tracking-[-0.03em]">관련 기사</h2>
309:               <p class="mt-3 text-gray-400 leading-7">
310:                 전국대학교로켓연합회와 관련된 외부 기사입니다.
311:               </p>
312:             </div>
313: 
314:             <div class="relative w-full max-w-[1100px] mx-auto z-10" id="news-hero-section">
315:               <div class="flex flex-col lg:flex-row relative">
316:                 
317:                 <!-- Swiper Container (Left Side, FOREGROUND) -->
318:                 <div class="w-full lg:w-[55%] relative z-20">
319:                   <div class="swiper news-swiper rounded-3xl overflow-hidden aspect-[16/10] bg-gray-900 shadow-2xl">
320:                     <div class="swiper-wrapper" id="news-swiper-wrapper">
321:                       <!-- Slides will be injected here by JS -->
322:                     </div>
323:                   </div>
324:                 </div>
325: 
326:                 <!-- Text Box Container (Right Side, BACKGROUND) -->
327:                 <div class="w-full lg:w-[92%] lg:absolute lg:right-0 lg:top-12 lg:-bottom-8 z-10 mt-6 lg:mt-0">
328:                   <div class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8 lg:pt-14 lg:pb-12 lg:pr-12 lg:pl-[56%] shadow-2xl flex flex-col justify-between h-full">
329:                     <div>
330:                       <h3 class="text-2xl font-bold text-white leading-snug mb-4 line-clamp-2" id="news-hero-title"></h3>
331:                       <p class="text-gray-400 leading-7 line-clamp-3" id="news-hero-summary"></p>
332:                     </div>
333:                     
334:                     <div class="mt-8 flex flex-col sm:flex-row sm:items-end justify-between gap-6">
335:                       <div>
336:                         <span class="text-sm text-gray-500 block mb-2" id="news-hero-date"></span>
337:                         <a href="#" target="_blank" rel="noopener noreferrer" id="news-hero-link" class="inline-flex items-center gap-1 text-sm font-semibold text-white hover:text-gray-300 transition">
338:                           기사 보기
339:                           <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
340:                         </a>
341:                       </div>
342:                       
343:                       <!-- Swiper Controls -->
344:                       <div class="flex items-center gap-4">
345:                         <div class="flex items-center gap-2 text-gray-400 font-mono text-sm">
346:                           <span id="news-hero-current" class="text-white">1</span>
347:                           <span class="w-8 h-[1px] bg-gray-600"></span>
348:                           <span id="news-hero-total">3</span>
349:                         </div>
350:                         <div class="flex gap-2">
351:                           <button type="button" class="news-prev w-10 h-10 rounded-full border border-white/15 bg-white/5 hover:bg-white/10 flex items-center justify-center text-white transition disabled:opacity-50 disabled:cursor-not-allowed">
352:                             <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
353:                           </button>
354:                           <button type="button" class="news-next w-10 h-10 rounded-full border border-white/15 bg-white/5 hover:bg-white/10 flex items-center justify-center text-white transition disabled:opacity-50 disabled:cursor-not-allowed">
355:                             <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
356:                           </button>
357:                         </div>
358:                       </div>
359:                     </div>
360:                   </div>
361:                 </div>
362: 
363:               </div>
364:             </div>
365:           </div>
366:         </section>
367: 
368:         <!-- NURA OVERVIEW -->
369:         <section class="w-full bg-black border-t border-white/5 border-b border-white/5">
370:           <div class="max-w-7xl mx-auto px-4 md:px-8 py-20">
371:             <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-4 mb-10">
372:               <div>
373:                 <p class="text-sm uppercase tracking-[0.2em] text-white/50 mb-3">NURA OVERVIEW</p>
374:                 <h2 class="text-3xl md:text-4xl font-bold text-white tracking-[-0.03em]">숫자로 보는 NURA</h2>
375:                 <p class="mt-3 text-gray-400 leading-7 max-w-2xl">
376:                   연합회의 현재 규모와 활동 현황을 한눈에 볼 수 있도록 주요 지표를 정리했습니다.
377:                 </p>
378:               </div>
379:             </div>
380: 
381:             <div id="stats-list" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5"></div>
382:           </div>
383:         </section>
384: 
385:         <!-- CURRENT PARTNERS -->
386:         <section class="border-t border-white/10 border-b border-white/10 bg-black">
387:           <div class="max-w-7xl mx-auto px-4 md:px-8 py-16 md:py-20">
388:             <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-4 mb-10">
389:               <div class="max-w-3xl">
390:                 <p class="text-sm uppercase tracking-[0.2em] text-white/50 mb-3">CURRENT PARTNERS</p>
391:                 <h2 class="text-3xl md:text-4xl font-bold tracking-[-0.03em] text-white">현재 함께하는 파트너</h2>
392:                 <p class="mt-3 text-gray-400 leading-7 max-w-2xl">
393:                   NURA의 활동을 지원해주신 기업 및 기관입니다.
394:                 </p>
395:               </div>
396:             </div>
397: 
398:             <div id="sponsor-wall" class="mt-4 px-8 py-6 grid grid-cols-[repeat(auto-fit,minmax(200px,1fr))] gap-8">
399:               <div class="bg-white rounded-xl shadow p-6 flex flex-col items-center justify-center">
400:                 <a href="https://www.koreanair.com" target="_blank" rel="noopener noreferrer">
401:                   <img src="source/partnership/koreanair.png" alt="대한항공 로고" class="max-w-full max-h-24 object-contain" loading="lazy" decoding="async">
402:                 </a>
403:               </div>
404: 
405:               <div class="bg-white rounded-xl shadow p-6 flex flex-col items-center justify-center">
406:                 <a href="https://www.innospc.com" target="_blank" rel="noopener noreferrer">
407:                   <img src="source/partnership/innospace.png" alt="이노스페이스 로고" class="max-w-full max-h-24 object-contain" loading="lazy" decoding="async">
408:                 </a>
409:               </div>
410: 
411:               <div class="bg-white rounded-xl shadow p-6 flex flex-col items-center justify-center">
412:                 <a href="https://www.kari.re.kr" target="_blank" rel="noopener noreferrer">
413:                   <img src="source/partnership/kari.jpg" alt="한국항공우주연구원 로고" class="max-w-full max-h-24 object-contain" loading="lazy" decoding="async">
414:                 </a>
415:               </div>
416: 
417:                <div class="bg-white rounded-xl shadow p-6 flex flex-col items-center justify-center">
418:                 <a href="https://www.ligpoongsan.co.kr" target="_blank" rel="noopener noreferrer">
419:                   <img src="source/partnership/ligpoongsan.png" alt="LIG풍산 로고" class="max-w-full max-h-24 object-contain" loading="lazy" decoding="async">
420:                 </a>
421:               </div>
422: 
423:               <!--
424:               <div class="bg-white rounded-xl shadow p-6 flex flex-col items-center justify-center">
425:                 <a href="https://www.kasa.go.kr/eng/index.do" target="_blank" rel="noopener noreferrer">
426:                   <img src="source/partnership/kasa.png" alt="우주항공청 로고" class="aspect-[2/1] w-48 max-w-full object-contain" loading="lazy" decoding="async">
427:                 </a>
428:               </div>
429:               -->
430: 
431:             </div>
432:           </div>
433:         </section>
434:       </main>
435: 
436:       <div data-shared-footer></div>
437:     </div>
438: 
439:     <script>
440:       (function () {
441:         const lines = document.querySelectorAll(".hero-reveal .reveal-line");
442: 
443:         function revealHeroText() {
444:           lines.forEach((line, index) => {
445:             setTimeout(() => {
446:               line.classList.add("is-visible");
447:             }, 220 + index * 180);
448:           });
449:         }
450: 
451:         if (document.readyState === "loading") {
452:           document.addEventListener("DOMContentLoaded", revealHeroText, { once: true });
453:           return;
454:         }
455: 
456:         revealHeroText();
457:       })();
458:     </script>
459: 
460:     <script>
461:       (function () {
462:         const slides = document.querySelectorAll(".slide-img");
463:         const progressFill = document.querySelector(".hero-progress-fill");
464:         const toggleButton = document.querySelector(".hero-progress-toggle");
465: 
466:         if (!slides.length || !progressFill) return;
467: 
468:         const slideDuration = 5000;
469:         let current = 0;
470:         let isPaused = false;
471: 
472:         let slideStartTime = performance.now();
473:         let elapsedBeforePause = 0;
474:         let rafId = null;
475: 
476:         function loadSlide(img) {
477:           if (!img || img.src || !img.dataset.src) return;
478:           img.src = img.dataset.src;
479:         }
480: 
481:         function preloadUpcomingSlides(idx) {
482:           const preload = () => {
483:             loadSlide(slides[(idx + 1) % slides.length]);
484:             loadSlide(slides[(idx + 2) % slides.length]);
485:           };
486: 
487:           if ("requestIdleCallback" in window) {
488:             requestIdleCallback(preload, { timeout: 1600 });
489:           } else {
490:             setTimeout(preload, 400);
491:           }
492:         }
493: 
494:         function showSlide(idx) {
495:           loadSlide(slides[idx]);
496: 
497:           slides.forEach((img, i) => {
498:             img.style.opacity = i === idx ? "1" : "0";
499:             img.style.zIndex = i === idx ? "1" : "0";
500:           });
501: 
502:           current = idx;
503:           slideStartTime = performance.now();
504:           elapsedBeforePause = 0;
505:           progressFill.style.width = "0%";
506:           preloadUpcomingSlides(idx);
507:         }
508: 
509:         function nextSlide() {
510:           showSlide((current + 1) % slides.length);
511:         }
512: 
513:         function updateProgress(now) {
514:           if (isPaused) return;
515: 
516:           const elapsed = elapsedBeforePause + (now - slideStartTime);
517:           const progress = Math.min(elapsed / slideDuration, 1);
518: 
519:           progressFill.style.width = `${progress * 100}%`;
520: 
521:           if (progress >= 1) {
522:             nextSlide();
523:           }
524: 
525:           rafId = requestAnimationFrame(updateProgress);
526:         }
527: 
528:         function startLoop() {
529:           cancelAnimationFrame(rafId);
530:           slideStartTime = performance.now();
531:           rafId = requestAnimationFrame(updateProgress);
532:         }
533: 
534:         function pauseLoop() {
535:           cancelAnimationFrame(rafId);
536:           elapsedBeforePause += performance.now() - slideStartTime;
537:         }
538: 
539:         function resumeLoop() {
540:           slideStartTime = performance.now();
541:           rafId = requestAnimationFrame(updateProgress);
542:         }
543: 
544:         function setPausedState(paused) {
545:           isPaused = paused;
546: 
547:           if (isPaused) {
548:             pauseLoop();
549:             toggleButton.classList.add("is-play");
550:             toggleButton.setAttribute("aria-label", "슬라이드 재생");
551:           } else {
552:             toggleButton.classList.remove("is-play");
553:             toggleButton.setAttribute("aria-label", "슬라이드 일시정지");
554:             resumeLoop();
555:           }
556:         }
557: 
558:         if (toggleButton) {
559:           toggleButton.addEventListener("click", function () {
560:             setPausedState(!isPaused);
561:           });
562:         }
563: 
564:         showSlide(0);
565:         startLoop();
566:       })();
567:     </script>
568: 
569:     <script>
570:       (function () {
571:         const data = window.NURA_DATA;
572:         if (!data) return;
573: 
574:         const swiperWrapper = document.getElementById("news-swiper-wrapper");
575:         const statsContainer = document.getElementById("stats-list");
576: 
577:         if (swiperWrapper && typeof Swiper !== "undefined" && data.newsItems) {
578:           swiperWrapper.innerHTML = data.newsItems
579:             .map(
580:               (item) => `
581:                 <div class="swiper-slide cursor-pointer group">
582:                   <div class="w-full h-full overflow-hidden">
583:                     <img
584:                       src="${item.image}"
585:                       alt="${item.title}"
586:                       class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
587:                       loading="lazy"
588:                       decoding="async"
589:                     />
590:                   </div>
591:                 </div>
592:               `
593:             )
594:             .join("");
595: 
596:           const titleEl = document.getElementById("news-hero-title");
597:           const summaryEl = document.getElementById("news-hero-summary");
598:           const dateEl = document.getElementById("news-hero-date");
599:           const linkEl = document.getElementById("news-hero-link");
600:           const curEl = document.getElementById("news-hero-current");
601:           const totEl = document.getElementById("news-hero-total");
602: 
603:           if (totEl) totEl.textContent = data.newsItems.length;
604: 
605:           const updateTextBox = (index) => {
606:             const item = data.newsItems[index];
607:             if (!item) return;
608:             if (titleEl) titleEl.textContent = item.title;
609:             if (summaryEl) summaryEl.textContent = item.summary;
610:             if (dateEl) dateEl.textContent = item.date;
611:             if (linkEl) linkEl.href = item.href;
612:             if (curEl) curEl.textContent = index + 1;
613:           };
614: 
615:           if (data.newsItems.length > 0) updateTextBox(0);
616: 
617:           const newsSwiper = new Swiper(".news-swiper", {
618:             loop: true,
619:             speed: 600,
620:             autoplay: {
621:               delay: 5000,
622:               disableOnInteraction: false,
623:             },
624:             navigation: {
625:               nextEl: ".news-next",
626:               prevEl: ".news-prev",
627:             },
628:             on: {
629:               slideChange: function () {
630:                 updateTextBox(this.realIndex);
631:               },
632:             },
633:           });
634: 
635:           const slides = swiperWrapper.querySelectorAll('.swiper-slide');
636:           slides.forEach((slide) => {
637:              slide.addEventListener('click', () => {
638:                 const itemIdx = slide.getAttribute('data-swiper-slide-index');
639:                 const idx = itemIdx !== null ? parseInt(itemIdx, 10) : 0;
640:                 const item = data.newsItems[idx];
641:                 if(item && item.href) window.open(item.href, '_blank', 'noopener,noreferrer');
642:              });
643:           });
644:         }
645: 
646:         if (statsContainer) {
647:           statsContainer.innerHTML = data.overviewStats
648:             .map(
649:               (item) => `
650:                 <article class="rounded-3xl border border-white/10 bg-white/5 p-6 md:p-7">
651:                   <p class="text-sm text-gray-500">${item.basis}</p>
652:                   <h3 class="mt-3 text-lg font-semibold text-gray-200">${item.label}</h3>
653:                   <p class="mt-5 text-4xl md:text-5xl font-extrabold tracking-[-0.03em] text-white">
654:                     <span class="count-up text-white" data-target="${item.value}">0</span><span class="text-white">${item.unit}</span>
655:                   </p>
656:                 </article>
657:               `
658:             )
659:             .join("");
660: 
661:           const counters = statsContainer.querySelectorAll(".count-up");
662:           const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
663: 
664:           function animateCounter(el) {
665:             const target = parseInt(el.dataset.target, 10);
666:             const duration = 1400;
667:             const startTime = performance.now();
668: 
669:             function update(now) {
670:               const progress = Math.min((now - startTime) / duration, 1);
671:               const eased = 1 - Math.pow(1 - progress, 3);
672:               const current = Math.floor(target * eased);
673: 
674:               el.textContent = current.toLocaleString();
675: 
676:               if (progress < 1) {
677:                 requestAnimationFrame(update);
678:               } else {
679:                 el.textContent = target.toLocaleString();
680:               }
681:             }
682: 
683:             requestAnimationFrame(update);
684:           }
685: 
686:           if (prefersReducedMotion) {
687:             counters.forEach((el) => {
688:               el.textContent = parseInt(el.dataset.target, 10).toLocaleString();
689:             });
690:           } else {
691:             const observer = new IntersectionObserver(
692:               (entries, obs) => {
693:                 entries.forEach((entry) => {
694:                   if (entry.isIntersecting) {
695:                     animateCounter(entry.target);
696:                     obs.unobserve(entry.target);
697:                   }
698:                 });
699:               },
700:               {
701:                 threshold: 0.35
702:               }
703:             );
704: 
705:             counters.forEach((counter) => observer.observe(counter));
706:           }
707:         }
708:       })();
709:     </script>
710:   </body>
711: </html>"""

lines = []
for line in content.split('\n'):
    m = re.match(r'^\d+: (.*)$', line)
    if m:
        lines.append(m.group(1))
    elif re.match(r'^\d+:$', line):
        lines.append("")

with open("index.html", "w") as f:
    f.write('\n'.join(lines) + '\n')
