<template>
  <div class="content">
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/cadastro">Cadastro</router-link></li>
      </ul>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {};
</script>

<style>
.content {
  font-family: "Courier New", Courier, monospace;
  width: 90%;
  margin: 0 auto;
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline;
}
</style>
