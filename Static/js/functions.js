d3.csv('../Data/Minimum_Wage_Data.csv').then(function(min_wage_data) {
    console.log('Min Wage Data', min_wage_data);

    var min_wage_state = min_wage_data.map(data => data.State);
    var min_wage_year = min_wage_data.map(data => data.Year);
    var state_min_wage = min_wage_data.map(data => data.State_Minimum_Wage);
    var fed_min_wage = min_wage_data.map(data => data.Federal_Minimum_Wage);
    var state_min_wage_2020 = min_wage_data.map(data => data.State_Minimum_Wage_2020_Dollars);
    var fed_min_wage_2020 = min_wage_data.map(data => data.Federal_Minimum_Wage_2020_Dollars);
    console.log('States', min_wage_state)
    console.log('year', min_wage_year);
    console.log('state_min', state_min_wage);
    console.log('fed min', fed_min_wage);
    console.log('2020 state min', state_min_wage_2020)
    console.log('2020 fed min', fed_min_wage_2020)

    d3.csv('../Data/Education.csv').then(function(educ_data) {
        console.log('Educ Data:', educ_data);
    });

    d3.csv('../Data/GDP.csv').then(function(gdp_data){
        console.log('GDP data', gdp_data);
    });

    d3.csv('../Data/USUnemployment.csv').then(function(unemploy_data) {
        console.log('Unemployment data', unemploy_data);
    });
})