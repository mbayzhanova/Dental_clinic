$(document).ready(function() {
    $("#doctorSelect").change(function(e){
        let doctorId = $(this).find(":selected").val()
        $.ajax({
            url:"http://localhost:8000/doctors/" + doctorId,
            type: "GET",
            success: function(streets){
                let worktimeSelect = $("#worktime");
                worktimeSelect.html('')
                streets.forEach((element) =>{
                    worktimeSelect.append(`
                        <p>${element.day_of_week.name} <b> ${element.working_time.name}</b></p>
                        `)
                })
            }
        })
    });

    var selectedDate = null;
    var selectedTime = null;
  

    $("#datepicker").change(function (event) {
        selectedDate = event.currentTarget.value;
    });

    $("#timeSelect").change(function (event) {
        selectedTime = event.currentTarget.value;
        let orderTimeSelect = $("#orderTime");
        orderTimeSelect.val(selectedDate + ' ' + selectedTime);
    });
    

    $("#timeSelect").change(function(e){
        let doctorId = $(this).find(":selected").val()
        $.ajax({
            url:"http://localhost:8000/doctors/" + doctorId,
            type: "GET",
            success: function(streets){
                let worktimeSelect = $("#work2");
                worktimeSelect.html('')
                streets.forEach((element) =>{
                    worktimeSelect.append(`
                        <p>${element.day_of_week.name} <b> ${element.working_time.name}</b></p>
                        `)
                })
            }
        })
    });
})