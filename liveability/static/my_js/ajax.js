/*** Created by Pharrell_WANG on 28/3/2017.*/var frm = $('#s_form');frm.submit(function () {    $.ajax({        type: frm.attr('method'),        url: frm.attr('action'),        data: frm.serialize(),        contentType: "application/json",        success: function (response) {            $("#score_cr").html(response["cr"]);            $("#score_dining").html(response["dining"]);            $("#score_housing").html(response["housing"]);            $("#score_edu").html(response["edu"]);            $("#employment").html(response["employment"]);            $("#air_quality").html(response["air_quality"]);            $("#amenities").html(response["amenities"]);            $("#value_best_dis").html(response["best_dis"]);            $("#value_best_sco").html(response["best_sco"]);            $("#value_popu").html(response["popu"]);            $("#value_area").html(response["area"]);        },        error: function () {            alert("error loading json ")        }    });    return false;});