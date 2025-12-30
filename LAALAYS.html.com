<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LAALAYS.COM</title>
    <link rel="stylesheet" href="style.css">
    <link rel="shortcut icon" href="./images/logo.ico" type="image/x-icon">
</head>
<body>
    <nav>
        <H2>LAALAYS.COM</H2>
        <ul>
            <li><a href="#">HOME</a></li>
            <li><a href="#">ABOUT</a></li>
            <li><a href="#">COURSES</a></li>
            <li><a href="#">TEAM</a></li>
            <li><a href="#">CONTACT</a></li>
        </ul>
    </nav>

    <div class="hero">
        <h2>WELCOME TO ORBIT COLLEGE</h2>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. At, accusantium.</p>
        <button>SEE MORE</button>
    </div>

    <section id="about">
        <div class="heading">
            <h2>ABOUT Us</h2>
        </div>

        <div class="container">
            <div class="about-content">
                <h2>WELCOME TO <span>ORBIT COLLEGE</span> </h2>
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Debitis, pariatur ut nulla, totam aspernatur dolorem soluta dolores quos dignissimos, minima vel rem cumque necessitatibus ad delectus ipsam aliquid! Facili quos architecto voluptates laborum! Amet, dolorum harum, reiciendis, nihil ex tempore culpa voluptates cum eligendi pariatur voluptas quidem praesentium voluptatem odio doloribus inventore nisi excepturi temporibus? Ex iste quibusdam iusto dolore voluptatum, minima corrupti dolores architecto, consequuntur mollitia, similique delectus! Veniam consequatur eum aliquid eveniet iusto iste dicta quo itaque possimus eaque sapiente velit, commodi ut natus cupiditate maiores, repellendus illum?</p>
                <button>SEE MORE</button>
            </div>
        <div class="about-image">
            <img src="./image/2.jpg" alt="">
        </div>
    </div>
    </section>




<!--start course section -->
<div id="course">
<div class="heading">
<h2>OUR COURSES</h2>
</div>

<div class="course-container">

    <div class="box">
        <img src="imagesWEB.png" alt="">
        <h2>WEB DEVELOPMENT</h2>
        <p>qaybtan waxaad ku baranaysaan dhisisdda iyo sameynta website-yada 
<span>html , CSS & JS</span></p>
            <button class="btn"><a href="#">SEE MORE</a></button>
        </div>
        <div class="box">
            <img src="images/TECHINCAL.png" alt="">
            <h2> TECHNICAL ENGINEER</h2>
            <P>qaybtan waxaad ku baranaysaa furfurka iyo xidhxidhka computerska

<span> HARDWARE, OS & TOT</span></P>
             <button class="btn"><a href="#"> SEE MORE</a></button>
              <div class="box">
                <img src="images/GRAPHIC.png" alt="">
                <h2> GRAPHIC DESIGNER</h2>
                <p>qaybtan waxaad ku baranaysaa sameynta iyo hagaajinta designerka
<span>PHOTOSHOP, ILLUSRATOR</span></p>

            <button class="btn"><a href="#">SEE MORE</a><button>
                <div>

                 
                <div class="box">  
                    <img src="images/local-area-network.png" alt="">
                    <h2>NETWORKING</h2>
                    <P>QAYTAN WAXAAD KU BARANAYSAA ISKU XIDHAK COMPUTERS SI AY XOG U 
            WADAADAAN</P>

                        <button class="btn"><a href="#">SEE MORE</a><button>
                    <div>
                         <div class="box">
                             <img src="images/coding.png" alt="">
                             <h2>PROGRAMING</h2>
                             <p>WAXAAD QAYBTAN KU BARANAYSAA LUUQADDAHA HIGT LEVEL LANGUAGE
<span>C++,C#</span></p>      <button class="btn"><a href="#">SEE MORE</a><button>



                         </div>

                        <div class="box">
                            <img src="image/database-storage.png" alt="">
                            <h2>DATABASE<h2>
                            <p>QAYBTAN WAXAAD KU BARANAYSAA SIDA LOO MAAMULO DATABASESKA
<span> SQL, MYSQL</span><p>                                
              <button class="btn"><a href="#">SEE MORE</a><button>
              </div>

              </div>
            </div>

            <!-- end course section-->



            <footer>

            <div class="button-bar">
                <p>&copy; 2025 LAALAYS.COM ALL RIGHT RESERVED</P>
                 <a href="https://m.facebook.com/sallosenior/" target="_blank"><img
            src="./icons/instagram.svg" alt=""></a>
                 </d>

                 </footer>     



</body>
</html>
