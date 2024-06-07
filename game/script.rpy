# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ms = Character("Mbok Srini")
define r = Character("Raksasa")
define tm = Character("Timun Mas")
define p = Character("Petapa")

transform pop:
 ease .06 yoffset 24
 ease .06 yoffset -24
 ease .05 yoffset 20
 ease .05 yoffset -20
 ease .04 yoffset 16
 ease .04 yoffset -16
 ease .03 yoffset 12
 ease .03 yoffset -12
 ease .02 yoffset 8
 ease .02 yoffset -8
 ease .01 yoffset 4
 ease .01 yoffset -4
 ease .01 yoffset 0

# The game starts here.

label start:
    scene village_day with dissolve
    play music "Cobblestone Village.mp3"
    
    show mbok_srini at center
    show mbok_srini at pop
    "Alkisah di sebuah desa di daerah Jawa Tengah, hidup seorang janda paruh baya yang bernama Mbok Srini. Sejak ditinggal oleh suaminya beberapa tahun, ia hidup sebatang kara, tak memiliki anak."
    "Kesepian menghantui harinya. Dia berdoa dengan penuh harap, meminta keajaiban dari Tuhan agar dikaruniai seorang anak."
    "Namun, harapannya pupus karena suaminya telah meninggal dunia. Mbok Srini hanya bisa menunggu keajaiban."

    "Tiba suatu malam, dalam mimpinya..."
    scene black with dissolve
    
    show raksasa at center
    show raksasa at pop
    r "{i}Hey Mbok Srini, pergilah ke daerah dekat pohon besar! ambilah bungkusan di bawah pohon besar besok pagi. Itu akan memberimu kebahagiaan yang kamu cari-cari.{/i}"
    
    scene black with dissolve
    ms "Hah aku mungkin sudah gila, namun aku harus mencari tahu apakah mimpiku barusan itu asli atau palsu!"
    "Mbok Srini terbangun di pagi hari dan dengan penuh harapan berjalan menuju hutan mencari pohon besar yang dimaksud."
    scene giant_tree with dissolve
    show mbok_srini at center
    show mbok_srini at pop
    ms "Itu dia pohon besar yang dimaksud di mimpiku."
    show mbok_srini at pop
    ms "Apakah ini benar-benar akan membawa kebahagiaan padaku? aku berpikir-pikir apa maksudnya ya."
    
    "Dia menemukan suatu bungkusan yang isinya biji di bawah pohon besar itu."
    show mbok_srini at pop
    ms "Hah Biji ?!?!"
    show mbok_srini at pop
    ms "Apa maksud raksasa itu memberikanku sebutir biji timun ini?"

    "Tiba-tiba, raksasa itu muncul di hadapannya."
    hide mbok_srini
    show mbok_srini_sad at left
    show raksasa at right
    show raksasa at pop
    r "Ha Ha Ha..."
    
    "Mbok Srini pun terkejut sambil membalikkan badannya. Betapa terkejutnya ia karena raksasa itulah yang hadir dalam mimpinya. Ia pun menjadi ketakutan."
    show mbok_srini_sad at pop
    ms "Ampun, Tuan Raksasa! Jangan memakanku! Aku masih ingin hidup!"
    show raksasa at pop
    r "Hai, Mbok Srini! Jangan khawatir, kamu akan mendapatkan anak perempuan. Tanam biji timun itu dan jadikanlah keinginanmu menjadi nyata."
    show mbok_srini_sad at pop
    ms "Ba-ba-ba-Baik Tuan Raksasa!"
    show raksasa at pop
    r "Kalau begitu, segera tanam biji timun itu! Nanti kamu akan mendapatkan seorang anak perempuan. Tapi, ingat! Kamu harus menyerahkan anak itu kepadaku saat ia sudah dewasa. Karena anak itu akan kujadikan santapanku."
    show mbok_srini_sad at pop
    ms "Baiklah, aku setuju!"
    hide raksasa


    scene backyard with dissolve
    "Kemudian ia segera menanam biji timun itu di ladangnya. Dengan penuh harapan, setiap hari ia merawat tanaman itu dengan baik."
    scene backyard_blur with dissolve
    show mbok_srini at left
    show mbok_srini at pop
    ms "Walau terdengar gila, tapi aku akan tetap menjalankan perintah Raksasa, aku yakin ucapannya benar!"
    "Dua bulan kemudian, tanaman itu pun mulai berbuah. Namun anehnya, tanaman timun itu hanya berbuah satu."
    "Semakin hari buah timun menjadi semakin besar melebihi buah timun pada umumnya. Warnanya pun sangat berbeda, karena berwarna kuning keemasan. Ketika buah timun sudah masak, Mbok Srini memetiknya timun yang berat dengan susah payah ke gubuknya."

    scene born_inside_cucumber with dissolve
    "Betapa terkejutnya ia ketika membelah buah timun itu. Ia melihat seorang bayi perempuan yang sangat cantik. Saat akan menggendongnya, bayi itu tiba-tiba menangis."
    ms "njirrr..., benar-benar ada bayi di dalam timun ini!"
    tm "ngoa.. ngoa.. ngoa.."
    
    scene born_inside_cucumber_blur with dissolve
    show mbok_srini at left
    show mbok_srini at pop
    ms "Anugerah Tuhan yang luar biasa! Aku akan menyebutmu Timun Mas."
    show mbok_srini at pop
    ms "Cup… cup… cup..!!! Jangan menangis anakku sayang… Timun Mas!"

    scene village_day with dissolve
    show mbok_srini at center 
    
    "Ia merawat dan mendidik Timun Mas dengan rasa kasih sayang hingga tumbuh menjadi perempuan yang cantik."
    show timun_mas at left
    "Mbok Srini sangat bangga, karena selain cantik, Timun Mas juga memiliki kecerdasan yang luar biasa dan sifatnya yang baik. Oleh karena itu, ia sangat sayang kepadanya."
    
    scene old_ hag_sleep with dissolve
    "Namun, suatu malam, Mbok Srini bermimpi raksasa itu kembali."
    
    scene old_ hag_sleep_blur with dissolve
    show raksasa at right
    show raksasa at pop
    r "{i}Saatnya kamu menepati janjimu, Mbok Srini. Dalam seminggu, aku akan menjemput Timun Mas!{/i}"
    ms "{i}?!?!?!{/i}"
    hide raksasa
    
    scene village_day with dissolve
    play music "Harvest Moon Back to Nature Winter Theme.mp3"
    show mbok_srini_sad at center
    "Sejak itu, ia selalu duduk termenung seorang diri."
    "Hatinya pun menjadi sedih, karena ia akan berpisah dengan anak yang sangat disayanginya. Ia baru menyadari bahwa raksasa itu ternyata adalah raksasa yang jahat, karena Timun Mas akan dijadikan santapannya!"
    show timun_mas_sad at left
    "Melihat Mbok Srini sering duduk termenung, Timun Mas pun bertanya-tanya dalam hati. Suatu sore, Timun Emas memberanikan diri untuk menanyakan kegundahan hati yang dirasakan oleh ibunya."
    show timun_mas_sad at pop
    tm "Bu, mengapa akhir-akhir ini Ibu selalu tampak sedih?"
    "Sebenarnya Mbok Srini tidak ingin menceritakan penyebab kegundahan hatinya, karena dia tidak ingin anaknya itu ikut bersedih. Namun, karena terus didesak, akhirnya ia pun menceritakan asal-usul Timun Mas yang dirahasiakan selama ini."
    show mbok_srini_sad at pop
    ms "Maafkan Ibu, Anakku! Selama ini Ibu merahasiakan sesuatu kepadamu."
    show timun_mas_sad at pop
    tm "Rahasia apa Bu?"
    show mbok_srini_sad at pop
    ms "Ketahuilah, Timun Mas! Sebenarnya, kamu bukanlah anak kandung Ibu yang lahir dari rahim Ibu."
    hide timun_mas_sad
    show timun_mas at left
    show timun_mas at pop
    tm "pa mangsud?"
    
    "Mbok Srini pun menceritakan semua rahasia tersebut hingga mimpinya semalam bahwa sesosok raksasa akan datang menjemput anaknya itu untuk dijadikan santapan. Mendengar cerita itu, Timun Mas menjadi kaget seolah-olah tidak percaya."
    show timun_mas at pop
    tm "Aku tidak mau ikut bersama raksasa itu. Aku sangat sayang kepada Ibu yang telah mendidik dan membesarkan Timun"
    
    "Mendengar perkataan Timun Mas, Mbok Srini kembali termenung. Ia mencari cara agar anaknya selamat agar tidak menjadi santapan raksasa itu."
    scene black with dissolve
    "Sampai pada hari yang telah dijanjikan oleh raksasa itu, Mbok Srini belum juga menemukan jalan keluar. Hatinya pun mulai cemas. Dalam kecemasannya, tiba-tiba ia menemukan sebuah akal."
    
    "Ia menyuruh Timun Mas agar berpura-pura sakit. Dengan begitu, raksasa tidak akan mau menyantapnya. Saat matahari mulai senja, raksasa itu pun mendatangi gubuk Mbok Srini."
    scene village_evening with dissolve
    show mbok_srini at left
    show raksasa at right
    show raksasa at pop
    r "Hai, Perempuan Tua! Mana anak itu? Aku akan membawanya sekarang"
    show mbok_srini at pop
    ms "Maaf, Tuan Raksasa! Anak itu sedang sakit keras. Jika kamu menyantapnya sekarang, tentu dagingnya tidak enak. Bagaimana kalau tiga hari lagi kamu datang kemari?"
    show mbok_srini at pop
    ms "Saya akan menyembuhkan penyakitnya terlebih dahulu!"
    show raksasa at pop
    r "Wakatta, wasurenaide."
    show mbok_srini at pop
    ms "Yakusoku."
    hide raksasa
    
    scene black with dissolve
    "Setelah Mbok Srini berjanji, raksasa itu pun menghilang. Mbok Srini kembali bingung untuk mencari cara lain."
    "Akhirnya, ia menemukan cara yang untuk dapat menyelamatkan anaknya dari raksasa. Ia akan meminta bantuan kepada seorang pertapa yang tinggal di sebuah gunung."
    
    scene village_evening with dissolve
    show mbok_srini at center
    show mbok_srini at pop
    ms "Anakku! Besok pagi-pagi sekali Ibu akan pergi ke gunung untuk menemui seorang pertapa. Dia adalah teman almarhum suami Ibu. Barangkali dia dapat membantu kita untuk menghentikan niat jahat raksasa itu"
    show timun_mas_sad at left
    show timun_mas_sad at pop
    tm "Benar, Bu! Kita harus membinasakan raksasa itu. Karena aku tidak mau menjadi santapannya!"
    
    scene rumah_petapa with dissolve
    "Keesokan harinya, pagi-pagi sekali, berangkatlah Mbok Srini ke gunung itu. Sesampainya di sana, ia langsung menemui pertapa itu dan menyampaikan maksud kedatangannya."
    show mbok_srini at left
    show mbok_srini at pop
    ms "Maaf, Tuan Pertapa! Maksud kedatangan saya kemari ingin meminta bantuan kepada Tuan."
    show petapa at right
    show petapa at pop
    p "Apa yang bisa kubantu, Mbok Srini?"
    
    "Mbok Srini pun menceritakan masalah yang sedang dihadapi anaknya. Mendengar cerita Mbok Srini, pertapa itu pun bersedia membantu."
    p "Baiklah, tunggu di sini sebentar"
    hide petapa
    "petapa itu seraya berjalan masuk ke dalam ruang rahasianya"
    
    scene bundles_of_cloth with dissolve
    "Tak berapa lama, pertapa itu kembali sambil membawa tiga buah bungkusan kecil, lalu menyerahkannya kepada Mbok Srini."
    scene bundles_of_cloth_blur with dissolve
    show petapa at right
    show petapa at pop
    p "Berikanlah bungkusan ini kepada anakmu. Ketiga bungkusan ini masing-masing berisi biji timun, jarum, dan terasi. Jika raksasa itu mengejarnya, suruh sebarkan isi bungkusan ini!"
    menu:
        "Menerima bungkusan":
            jump good_ending
        "Menolak bungkusan":
            jump bad_ending

label good_ending:
    show mbok_srini at left
    show mbok_srini at pop
    ms "sankyu"
    "Setelah mendapat penjelasan itu, Mbok Srini pulang membawa keempat bungkusan tersebut."
    
    scene village_day with dissolve
    "Setiba di gubuknya, Mbok Srini menyerahkan keempat bungkusan itu dan menjelaskan tujuannya kepada Timun Mas. Kini, hati Mbok Srini mulai agak tenang, karena anaknya sudah mempunyai senjata untuk melawan raksasa itu."
    play music "American Venom.mp3"
    
    "Dua hari kemudian, Raksasa itu pun datang untuk menagih janjinya kepada Mbok Srini. Ia sudah tidak sabar lagi ingin membawa dan menyantap daging Timun Mas."
    show raksasa at right
    show raksasa at pop
    r "Hai, perempuan tua! Kali ini kamu harus menepati janjimu. Jika tidak, kamu juga akan kujadikan santapanku!"
    show mbok_srini at center
    show timun_mas_sad at left
    "Mbok Srini tidak gentar lagi menghadapi ancaman itu. Dengan tenang, ia memanggil Timun Mas agar keluar dari dalam gubuk. Tak berapa lama, Timun Emas pun keluar lalu berdiri di samping ibunya."
    show mbok_srini at pop
    ms "Jangan takut, Anakku! Jika raksasa itu akan menangkapmu, segera lari dan ikuti petunjuk yang telah kusampaikan kepadamu!"
    show timun_mas_sad at pop
    tm "wakarimashita!"
    
    "Melihat Timun Mas yang benar-benar sudah dewasa, rakasasa itu semakin tidak sabar ingin segera menyantapnya"
    show raksasa at pop
    r "Towewew... alamak"
    "Ketika ia hendak menangkapnya, Timun Mas segera berlari sekencang-kencangnya."
    hide timun_mas_sad
    show raksasa at pop
    r "Nigasanai !"
    "Raksasa itu pun mengejarnya. Tak ayal lagi, terjadilah kejar-kejaran antara makhluk raksasa itu dengan Timun Mas."
    hide raksasa
    
    scene run_away_from orc with dissolve
    "Setelah berlari jauh, Timun Mas mulai kecapaian, sementara raksasa itu semakin mendekat."
    "Akhirnya, ia pun mengeluarkan bungkusan pemberian pertapa itu."
    scene run_away_from orc_blur with dissolve
    "Pertama-tama Timun Mas menebar biji timun yang diberikan oleh ibunya."
    show timun_mas_sad at left
    show timun_mas_sad at pop
    show raksasa at right
    tm "Fire in the hole!"
    show raksasa at pop
    r "Apa yang mau kau lakukan hah?!"
    
    scene entangled_by_roots with dissolve
    "Sungguh ajaib, hutan di sekelilingnya tiba-tiba berubah menjadi ladang timun. Dalam sekejap, batang timun tersebut menjalar dan melilit seluruh tubuh raksasa itu."
    "Namun, raksasa itu mampu melepaskan diri dan kembali mengejar Timun Mas."
    scene entangled_by_roots_blur with dissolve
    show timun_mas_sad at left
    show timun_mas_sad at pop
    show raksasa_bleeding at right
    tm "Keras kepala ya?!, baiklah rasakan bingkisan ku yang ke-2! Fire in the hole!"
    "Timun Emas pun segera melemparkan bungkusan yang berisi jarum."
    show raksasa_bleeding at pop
    r "Sialan! apa yang barusan kau lempar?!"
    
    scene stabbed_by_bamboos with dissolve
    "Dalam sekejap, jarum-jarum tersebut berubah menjadi rerumbunan pohon bambu yang tinggi dan runcing."
    "Namun, raksasa itu mampu melewatinya dan terus mengejar Timun Mas, walaupun kakinya berdarah-darah karena tertusuk bambu tersebut."
    scene stabbed_by_bamboos_blur with dissolve
    show timun_mas_sad at left
    show timun_mas_sad at pop
    show raksasa_bleeding at right
    tm "kusottare ga! rasakan senjata pamungkas ku! Fire in the hole!"
    show raksasa_bleeding at pop
    r "Lempar aja terus itu njirrr"
    "Dengan penuh keyakinan, ia pun melemparkan bungkusan terakhir yang berisi terasi."
    
    scene drowned_in_lava with dissolve
    "Seketika itu pula, tempat jatuhnya terasi itu tiba-tiba menjelma menjadi lautan lava yang mendidih."
    scene drowned_in_lava_blur with dissolve
    show raksasa_bleeding at center
    show raksasa_bleeding at pop
    r "Kisamaaaa!!!!"
    "Alhasil raksasa itu terkalahkan karena tercebur ke dalam lautan lumpur dan tewas seketika."
    
    scene black with dissolve
    "Maka selamatlah Timun Emas dari kejaran dan santapan raksasa itu."
    
    scene village_day with dissolve
    "Dengan sekuat tenaga, Timun Mas berlari kembali menuju rumahnya untuk menemui ibunya."
    show timun_mas at right
    show timun_mas at pop
    tm "Tadaima!!"
    show mbok_srini at center
    "Melihat anaknya selamat, Mbok Srini pun langsung berucap syukur kepada Tuhan Yang Mahakuasa"
    show mbok_srini at pop
    ms "Kau kembali selamat Timun!! Alhamdulillah!"
    "Sejak itu, Mbok Srini dan Timun Mas hidup berbahagia."
    "Good Ending"
    jump end_game

label bad_ending:
    show mbok_srini at left
    show mbok_srini at pop
    ms "Terimakasih sebelumnya wahai petapa, tetapi aku tidak bisa menerima bungkusan ini"
    show petapa at pop
    p "Mengapa kamu menolaknya mbok Srini?"
    show mbok_srini at pop
    ms "Semua ini terdengar tidak masuk akal, aku tidak bisa menerimanya begitu saja!"
    show petapa at pop
    p "Baiklah kalau begitu mau mu Mbok Srini, setidaknya aku sudah berusaha membantu"
    "Mbok Srini menolak untuk menerima bungkusan dari pertapa karena merasa bahwa itu tidak masuk akal. Ia pulang dengan tangan hampa."
    
    scene village_day with dissolve
    show raksasa at right
    show raksasa at pop
    r "Yo aku datang!"
    show mbok_srini at center
    show timun_mas_sad at left
    show timun_mas_sad at pop
    tm "Sial bu dia sudah datang! aku harus gimana ?!"
    show mbok_srini at pop
    ms "Ehh emmhh.. kabur, ya Kabur nak! lari sejauh mungkin!"
    show timun_mas_sad at pop
    tm "Tidak mungkin aku bisa kabur darinya tanpa persiapan apapun!"
    show raksasa at pop
    r "Kau pikir kau bisa kabur dariku ?!"
    show timun_mas_sad at pop
    tm "F this sh**, aku lari dulu Bu!"
    hide timun_mas_sad
    show mbok_srini at pop
    ms "Semoga kau berhasil nak!"
    show raksasa at pop
    r "Yare-yare... Beliau pikir beliau bisa kabur dariku dengan gampang hah? hahaha aku datang ~~~"
    hide raksasa
    
    scene caught_by_orc with dissolve
    "Sekencang apapun Timun Mas lari, dengan mudah raksasa bisa mengejarnya. Timun Mas tertangkap dan tidak dapat melarikan diri." 
    
    scene caught_by_orc_blur with dissolve
    show timun_mas_sad at left
    show timun_mas_sad at pop
    tm "Sialan lepaskan aku!"
    show raksasa at right
    show raksasa at pop
    r "Ketangkap ~~~"
    "Raksasa itu mengambilnya dan menghilang, meninggalkan Mbok Srini dalam kesedihan dan penyesalan yang mendalam."
    "Bad Ending"
    jump end_game

label end_game:
    scene black with dissolve
    "Selamat, akhir cerita."
    
    # This ends the game.

    return
