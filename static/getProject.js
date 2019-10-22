//获取用例信息
var ProjectInit = function () {

    var url = document.location;
    var pid =  url.pathname.split("/")[2];
//    alert(pid)
    $.post("/get_project_info/",
    {
//        alert(pid)
        pid: pid,
    },
    function (resp) {
        console.log("返回的结果", resp.data);
        var result = resp.data;
        console.log(result.name)
        //请求URL
        document.querySelector("#project_name").value = result.name;
        //请求头
        document.querySelector("#simple_desc").value = result.description;

    });

}




