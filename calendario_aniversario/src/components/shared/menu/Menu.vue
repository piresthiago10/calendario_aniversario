<template>
  <nav>
    <ul>
      <li v-for="rota in rotas">
        <router-link class="navbar" :to="rota.path ? rota.path : '/'">
          {{ rota.titulo }}
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  props: {
      rotas: {
          type: Array,
          required: true
      }
  }
};
</script>

<style scoped>

.navbar{
    text-decoration: none;
    color: #728C76;
}

.navbar:hover{
    color: #D2D9D3;
}

nav{
    width: 100%;
    height: 50px;
    border-bottom: 2px solid #D2D9D3;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 15px;
}

li {
    list-style: none;
    margin: 2px;
    padding: 10px;
    font-size: 20px;
    display: inline;
}
</style>