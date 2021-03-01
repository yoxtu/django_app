var vm = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        todos: []
    },
    mounted: function () {
        axios.get('{% url "for_view_function_get_todo()" %}').then(function (response) {
            for (var d in response.data) {
                var item = response.data[d];
                item.due = new Date(item.due);
                vm.todos.push(item);
            }
        })
            .catch(function (error) {
                console.log(error);
            })
            .then(function () {
            });
    },
    methods: {
        changeStatus: function (item) {
            item.done = !item.done;
        }
    }
})