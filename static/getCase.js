var TestCaseInit = function () {

    var url = document.location;
    var cid =  url.pathname.split("/")[2];

    $.post("/get_case_info/",
    {
        cid: cid,
    },
    function (resp, status) {
        console.log("返回的结果", resp.data);
        var result = resp.data;

        //请求URL
        document.querySelector("#req_url").value = resp.data.url;
        
        //请求方法
        if (result.method == 1){
            document.querySelector("#get").setAttribute("checked", "");
        }else if (result.method == 2) {
            document.querySelector("#post").setAttribute("checked", "");
        }else if (result.method == 3){
            document.querySelector("#put").setAttribute("checked", "");
        } else if (result.method == 4){
            document.querySelector("#delete").setAttribute("checked", "");
        }

        //请求头
        document.querySelector("#header").value = result.header;

        //请求参数类型
        if (result.parameter_type == 1) {
            document.querySelector("#form").setAttribute("checked", "");
        }
        else if (result.parameter_type == 2) {
            document.querySelector("#json").setAttribute("checked", "");
        }

        //请求参数的值
        document.querySelector("#parameter").value = result.parameter_body;
        
        //断言的类型
        if (result.assert_type == 1) {
            document.querySelector("#contains").setAttribute("checked", "");
        }
        else if (result.assert_type == 2) {
            document.querySelector("#mathches").setAttribute("checked", "");
        }

        //断言的值
        document.querySelector("#assert").value = result.assert_text;

        //用例的名称
        document.querySelector("#case_name").value = result.case_name;

        // 初始化菜单
        SelectInit(result.project_id, result.module_id);

    });

}
