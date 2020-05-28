<template>
    <div class="rings">
        <div class="ring ring1"></div>
        <div class="ring ring2"></div>
        <div class="ring ring3"></div>
        <div class="ring ring4"></div>        
    </div>
</template>

<script></script>

<style scoped>
    * {
        background-image: none;
        background-size: cover;
    }
    /* .rings {
        margin-top: 20%;
        display: grid;
        grid-area: rings;
        grid-template-rows: 2fr 1fr 1fr 5fr 1fr 1fr 2fr;
        grid-template-areas: 
            "." 
            "ring1"
            "ring2"
            "."
            "ring3"
            "ring4"
            ".";
    } */
    .ring {
        display: grid;
        grid-area: ring;
        width: 120%;
        min-width: 15px;
        height: 30%;
        margin-left: 40%;
        /* background-color: rgba(254, 255, 254, 0.808); */
        background-color: #c2f8b4;  /* fallback for old browsers */
        background-color: -webkit-linear-gradient(to right, #c2f8b4, #dfe2df);  /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to right, #c2f8b4, #dfe2df); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        border-radius: 50px;
        box-shadow: 3px 3px 3px 2px rgba(8, 8, 8, 0.959);
    }
    .ring1 {
        display: grid;
        grid-area: ring1;
    }
    .ring2 {
        display: grid;
        grid-area: ring2;
    }
    .ring3 {
        display: grid;
        grid-area: ring3;
    }
    .ring4 {
        display: grid;
        grid-area: ring4;
    }    
</style>
