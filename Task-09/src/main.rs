fn main() {
    let response = reqwest::blocking::get("https://crypto.com/price").unwrap().text().unwrap();
    let document = scraper::Html::parse_document(&response);

    let crypto_name = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
    let crypto_price = scraper::Selector::parse("div.css-b1ilzc").unwrap();
    let crypto_24h_change = scraper::Selector::parse("div.css-16q9pr7>p").unwrap(); 
    let crypto_mark_cap = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    // let crypto_market_cap = Selector::parse("td.css-1nh9lk8").unwrap();

    
    let crypto_rate = document.select(&crypto_24h_change).map(|x| x.inner_html());
    let crypto_title = document.select(&crypto_name).map(|x| x.inner_html());
    let crypto_prices = document.select(&crypto_price).map(|x| x.inner_html());
    let crypto_vol_cap = document.select(&crypto_mark_cap).map(|x| x.inner_html());
    
    // for element in document.select(&crypto_name) {
    //     let crypto_name_element = element.select(&crypto_name).next().expect("Could not select book name.");
    //     let name = crypto_name_element.value().attr("title").expect("Could not find title attribute.");

    //     let crypto_rate = element.select(&crypto_24h_change).next().expect("Could not find price");
    //     let rate = crypto_racd ..te.text().collect::<String>();

    //     let crypto_cost = element.select(&crypto_price).next().expect("Could not find book link element.");
    //     let cost = crypto_cost.value().attr("href").expect("Could not find href attribute");

    //     let crypto_24h_volume = 
    let mut mark_cap: Vec<String> = vec![String::new();0];
    let mut vol24: Vec<String> = vec![String::new();0];
    let mut price: Vec<String> = vec![String::new();0];
    let mut name: Vec<String> = vec![String::new();0];
    let mut rate: Vec<String> = vec![String::new();0];

    for i in crypto_title{name.push(i);}
    for i in crypto_prices{price.push(i);}
    for i in crypto_rate{rate.push(i);}

    
    let mut j = 1;
    for i in crypto_vol_cap {
        if j%2==0{
            mark_cap.push(i);
        }
        else {
        vol24.push(i);
        }
    j+=1;
    }

    // for element in document.select(&crypto_name) {

    // }
    let mut wtr = csv::Writer::from_path("crypto.csv").unwrap();
    wtr.write_record(&["Name", "Price", "24H change", "24H volume", "Market Cap"]).unwrap();
    for i in 0..50
    {
        wtr.write_record([&name[i],&price[i],&rate[i],&vol24[i],&mark_cap[i]]).ok();
        wtr.flush().ok();
    }
        

    //    println!("{:?} - {:?}",book_name, price);
    // }

}

