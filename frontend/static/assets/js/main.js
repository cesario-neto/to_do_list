function getDateAndTime() {
    const taskForm = document.querySelector('#taskForm');
    const date = document.querySelector('#date');
    const time = document.querySelector('#time');
    const dateTime = document.querySelector('#id_end_in');
    dateTimeHaveValue();


    function dateTimeHaveValue() {
        if (dateTime.value) {
            [date.value, time.value] = dateTime.value.split(' ')
            return true;
        };
        
        return false;
    }

    function setEndIn(e) {
        e.preventDefault();
        dateTime.value = `${date.value} ${time.value}`;
        e.currentTarget.submit();
    }

    taskForm.addEventListener('submit', setEndIn);

}

getDateAndTime();