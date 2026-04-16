<template>
    <div class="page">
        <section id="init">
            <div class="init__background">
                <span class="init__nav-logo">CASABOAVIDALONGA</span>
                <ul class="init__nav-links">
                    <li><a href="#cats">GATO</a></li>
                    <li><a href="#dogs">CACHORRO</a></li>
                    <li><a href="#identify">PLANTAS</a></li>
                </ul>
            </div>
        </section>

        <section id="cats">
        </section>

        <section id="dogs">
        </section>

        <section id="identify">
            <div class="init__identify">
                <div class="upload-container">
                    <input type="file" class="file-input" name="fileImport" @change="onFileChange">
                    <div class="text" v-if="plantName != ''">
                        <span>NOME: {{ plantName }}</span>
                        <span>BOA: {{ goodFor }}</span>
                    </div>
                    <button v-if="plantName == ''" class="button" @click="onSubmit">Identificar</button>
                    <img v-if="imageUrl" :src="imageUrl">
                </div>
            </div>

        </section>
    </div>
</template>

<script lang="ts" src="./Page.ts"></script>

<style lang="scss" src="./Page.scss"></style>

