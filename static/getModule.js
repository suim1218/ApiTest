//获取用例信息
var ModuleInit = function () {

    var url = document.location;
    var mid =  url.pathname.split("/")[2];
//    alert(pid)
    $.post("/get_module_info/",
    {

        mid: mid,
    },
    function (resp) {
        console.log("返回的结果", resp.data);
        var result = resp.data;
        console.log(result.name)

        document.querySelector("#module_name").value = result.name;
        //请求头
        document.querySelector("#simple_desc").value = result.description;
         // 初始化菜单
        SelectInit(result.id, mid);

    });

}




