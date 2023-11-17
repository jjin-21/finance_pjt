<template>
    <div>
        <div>
            <v-form @submit.prevent="searchMap(searchWord)">
                <!-- Vuetify selects -->
                <v-row>
                <v-col>
                    <v-select
                    v-model="selectedCity"
                    :items="cities"
                    label="도시 선택"
                    outlined
                    ></v-select>
                </v-col>
                <v-col>
                    <v-select
                    v-model="selectedDistrict"
                    :items="filteredDistricts"
                    label="구 선택"
                    outlined
                    ></v-select>
                </v-col>
                <v-col>
                    <v-select
                    v-model="selectedBank"
                    :items="banks"
                    label="은행 선택"
                    outlined
                    ></v-select>
                </v-col>
                <v-col>
                    <v-btn type="submit" color="teal darken-2" style="height:58px;">검색하기</v-btn>
                </v-col>
                </v-row>

                <!-- Submit button -->
                
            </v-form>
        </div>
        <!-- 다크모드에서 아래부터는 글자색 유지 -->
        <div class="map_wrap light-mode">
            <div id="map" ref="map" style="width:100%;height:700px;position:relative;overflow:hidden;"></div>
        
            <div id="menu_wrap" style="height:600px;" class="bg_white">
                <div class="option">
                    
                </div>
                <hr>
                <ul id="placesList"></ul>
                <div id="pagination"></div>
            </div>
        </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue';
  
//   const searchWord = ref('')

  //@@@@@@@@@@@@@ 시,구, 은행 검색 구현@@@@@@@@@@
    //추후 최신 행정구역 api나 DB로 다운받아서 리스트 만들기 + 은행목록도
    const banks = ['KB국민은행', '신한은행', '우리은행', '하나은행', 'NH농협은행', '기업은행'];
    const cities = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '경기도', '강원도', '충청북도','충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주도']
    const cityDistricts = {
    서울특별시: ['종로구', '중구','용산구','성동구','광진구','동대문구','중랑구','성북구','강북구','도봉구','노원구','은평구','서대문구','마포구','양천구','강서구','구로구','금천구','영등포구','동작구','관악구','서초구','강남구','송파구','강동구'],
    부산광역시: ['중구','서구','동구','영도구','부산진구','동래구','남구','북구','해운대구','사하구','금정구','강서구','연제구','수영구','사상구','기장군'],
    대구광역시: ['중구','동구','서구','남구','북구','수성구','달서구','달성군'],
    인천광역시: ['중구','동구','미추홀구','연수구','남동구','부평구','계양구','서구','강화군','옹진군'],
    광주광역시: ['동구','서구','남구','북구','광산구'],
    대전광역시: ['동구','중구','서구','유성구','대덕구'],
    울산광역시: ['중구','남구','동구','북구','울주군'],
    경기도: ['고양시','수원시','용인시','과천시','광명시','광주시','구리시','군포시','김포시','남양주시','동두천시','부천시','성남시','시흥시','안산시','안성시','안양시','양주시','여주시','오산시','의왕시','의정부시','이천시','파주시','평택시','포천시','하남시','화성시','가평군','양평군','연천군'],
    강원도: ['강릉시','동해시','삼척시','속초시','원주시','춘천시','태백시','고성군','양구군','양양군','영월군','인제군','정선군','철원군','평창군','홍청군','화천군','횡성군'],
    충청북도: ['제천시','청주시','충주시','괴산군','단양군','보은군','영동군','옥천군','음성군','증평군','진천군'],
    충청남도: ['계룡시','공주시','논산시','당진시','보령시','서산시','아산시','천안시','금산군','부여군','서천군','예산군','청양군','태안군','홍성군'],
    전라북도: ['군산시','김제시','남원시','익산시','전주시','정읍시','고창군','무주군','부안군','순창군','완주군','임실군','장수군','진안군'],
    전라남도: ['광양시','나주시','목포시','순천시','여수시','강진군','고흥군','곡성군','구례군','담양군','무안군','보성군','신안군','영광군','영암군','완도군','장성군','장흥군','진도군','함평군','해남군','화순군'],
    경상북도: ['경산시','경주시','구미시','김천시','문경시','상주시','안동시','영주시','영천시','포항시','고령군','군위군','봉화군','성주군','영덕군','영양군','예천군','울릉군','울진군','의성군','청도군','청송군','칠곡군'],
    경상남도: ['창원시','거제시','김해시','밀양시','사천시','양산시','진주시','통영시','거창군','고성군','남해군','산청군','의령군','창녕군','하동군','함안군','함양군','합천군'],
    제주도: ['서귀포시','제주시']
    }


    // 선택된 값들
    const selectedCity = ref('');
    const selectedDistrict = ref('');
    const selectedBank = ref('');

    const filteredDistricts = computed(() => {
    return cityDistricts[selectedCity.value] || [];
    });

    const searchWord = computed(() => {
        return `${selectedCity.value} ${selectedDistrict.value} ${selectedBank.value}`;
    });




  
  const map = ref(null);
  
  onMounted(() => {
    const kakao = window.kakao;
  
    
  
    // console.log(map.value);
  
    var container = map.value;
    var options = {
      center: new kakao.maps.LatLng(37.566826, 126.9786567),
      level: 3,
    };
  
    const mapInstance = new kakao.maps.Map(container, options);
    // console.log(mapInstance);
  
  }); // 끝
  
  
  const searchMap = function(searchWord) {
    const kakao = window.kakao;
  
    
  
    // console.log(map.value);
  
    var container = map.value;
    var options = {
      center: new kakao.maps.LatLng(37.566826, 126.9786567),
      level: 3,
    };
  
    const mapInstance = new kakao.maps.Map(container, options);
  
    var markers = [];
    
    // 장소 검색 객체를 생성합니다
    var ps = new kakao.maps.services.Places();  
  
    // 검색 결과 목록이나 마커를 클릭했을 때 장소명을 표출할 인포윈도우를 생성합니다
    var infowindow = new kakao.maps.InfoWindow({zIndex:1});
  
    // 키워드로 장소를 검색합니다
    searchPlaces();
  
    // 키워드 검색을 요청하는 함수입니다
    function searchPlaces() {
  
  
        if (!searchWord.replace(/^\s+|\s+$/g, '')) {
            alert('키워드를 입력해주세요!');
            return false;
        }
  
        // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다
        ps.keywordSearch(searchWord , placesSearchCB); 
    }
  
    // 장소검색이 완료됐을 때 호출되는 콜백함수 입니다
    function placesSearchCB(data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {
  
            // 정상적으로 검색이 완료됐으면
            // 검색 목록과 마커를 표출합니다
            displayPlaces(data);
  
            // 페이지 번호를 표출합니다
            displayPagination(pagination);
  
        } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
  
            alert('검색 결과가 존재하지 않습니다.');
            return;
  
        } else if (status === kakao.maps.services.Status.ERROR) {
  
            alert('검색 결과 중 오류가 발생했습니다.');
            return;
  
        }
    }
  
    // 검색 결과 목록과 마커를 표출하는 함수입니다
    function displayPlaces(places) {
  
        var listEl = document.getElementById('placesList'), 
        menuEl = document.getElementById('menu_wrap'),
        fragment = document.createDocumentFragment(), 
        bounds = new kakao.maps.LatLngBounds(), 
        listStr = '';
        
        // 검색 결과 목록에 추가된 항목들을 제거합니다
        removeAllChildNods(listEl);
  
        // // 지도에 표시되고 있는 마커를 제거합니다
        removeMarker();
        
        for ( var i=0; i<places.length; i++ ) {
  
            // 마커를 생성하고 지도에 표시합니다
            var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
                marker = addMarker(placePosition, i), 
                itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다
  
            // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
            // LatLngBounds 객체에 좌표를 추가합니다
            bounds.extend(placePosition);
  
            // 마커와 검색결과 항목에 mouseover 했을때
            // 해당 장소에 인포윈도우에 장소명을 표시합니다
            // mouseout 했을 때는 인포윈도우를 닫습니다
            (function(marker, title) {
                kakao.maps.event.addListener(marker, 'mouseover', function() {
                    displayInfowindow(marker, title);
                });
  
                kakao.maps.event.addListener(marker, 'mouseout', function() {
                    infowindow.close();
                });
  
                itemEl.onmouseover =  function () {
                    displayInfowindow(marker, title);
                };
  
                itemEl.onmouseout =  function () {
                    infowindow.close();
                };
            })(marker, places[i].place_name);
  
            fragment.appendChild(itemEl);
        }
  
        // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
        listEl.appendChild(fragment);
        menuEl.scrollTop = 0;
  
        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        mapInstance.setBounds(bounds);
    }
  
    // 검색결과 항목을 Element로 반환하는 함수입니다
    function getListItem(index, places) {
  
        var el = document.createElement('li'),
        itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
                    '<div class="info">' +
                    '   <h5>' + places.place_name + '</h5>';
  
        if (places.road_address_name) {
            itemStr += '    <span>' + places.road_address_name + '</span>' +
                        '   <span class="jibun gray">' +  places.address_name  + '</span>';
        } else {
            itemStr += '    <span>' +  places.address_name  + '</span>'; 
        }
                    
          itemStr += '  <span class="tel">' + places.phone  + '</span>' +
                    '</div>';           
  
        el.innerHTML = itemStr;
        el.className = 'item';
  
        return el;
    }
  
    // 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
    function addMarker(position, idx, title) {
        var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
            imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
            imgOptions =  {
                spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
                spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
                offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
            },
            markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
                marker = new kakao.maps.Marker({
                position: position, // 마커의 위치
                image: markerImage 
            });
  
        marker.setMap(mapInstance); // 지도 위에 마커를 표출합니다
        markers.push(marker);  // 배열에 생성된 마커를 추가합니다
  
        return marker;
    }
  
    // 지도 위에 표시되고 있는 마커를 모두 제거합니다
    function removeMarker() {
        for ( var i = 0; i < markers.length; i++ ) {
            markers[i].setMap(null);
        }   
        markers = [];
    }
  
    // 검색결과 목록 하단에 페이지번호를 표시는 함수입니다
    function displayPagination(pagination) {
        var paginationEl = document.getElementById('pagination'),
            fragment = document.createDocumentFragment(),
            i; 
  
        // 기존에 추가된 페이지번호를 삭제합니다
        while (paginationEl.hasChildNodes()) {
            paginationEl.removeChild (paginationEl.lastChild);
        }
  
        for (i=1; i<=pagination.last; i++) {
            var el = document.createElement('a');
            el.href = "#";
            el.innerHTML = i;
  
            if (i===pagination.current) {
                el.className = 'on';
            } else {
                el.onclick = (function(i) {
                    return function() {
                        pagination.gotoPage(i);
                    }
                })(i);
            }
  
            fragment.appendChild(el);
        }
        paginationEl.appendChild(fragment);
    }
  
    // 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수입니다
    // 인포윈도우에 장소명을 표시합니다
    function displayInfowindow(marker, title) {
        var content = '<div style="padding:5px;z-index:1; height:30px;">' + title + '</div>';
  
        infowindow.setContent(content);
        infowindow.open(mapInstance, marker);
    }
  
    // 검색결과 목록의 자식 Element를 제거하는 함수입니다
    function removeAllChildNods(el) {   
        while (el.hasChildNodes()) {
            el.removeChild (el.lastChild);
        }
    }
  
  
  
  
  
  
  
  
  
  
  } // 끝
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  </script>
  
  <style>
  
  
  
  .map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
  .map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
  .map_wrap {position:relative;width:100%;height:500px;}
  #menu_wrap {position:absolute;top:0;left:0;bottom:0;width:250px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 1;font-size:12px;border-radius: 10px;}
  .bg_white {background:#fff;}
  #menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
  #menu_wrap .option{text-align: center;}
  #menu_wrap .option p {margin:10px 0;}  
  #menu_wrap .option button {margin-left:5px;}
  #placesList li {list-style: none;}
  #placesList .item {position:relative;border-bottom:1px solid #888;overflow: hidden;cursor: pointer;min-height: 65px;}
  #placesList .item span {display: block;margin-top:4px;}
  #placesList .item h5, #placesList .item .info {text-overflow: ellipsis;overflow: hidden;white-space: nowrap;}
  #placesList .item .info{padding:10px 0 10px 55px;}
  #placesList .info .gray {color:#8a8a8a;}
  #placesList .info .jibun {padding-left:26px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;}
  #placesList .info .tel {color:#009900;}
  #placesList .item .markerbg {float:left;position:absolute;width:36px; height:37px;margin:10px 0 0 10px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat;}
  #placesList .item .marker_1 {background-position: 0 -10px;}
  #placesList .item .marker_2 {background-position: 0 -56px;}
  #placesList .item .marker_3 {background-position: 0 -102px}
  #placesList .item .marker_4 {background-position: 0 -148px;}
  #placesList .item .marker_5 {background-position: 0 -194px;}
  #placesList .item .marker_6 {background-position: 0 -240px;}
  #placesList .item .marker_7 {background-position: 0 -286px;}
  #placesList .item .marker_8 {background-position: 0 -332px;}
  #placesList .item .marker_9 {background-position: 0 -378px;}
  #placesList .item .marker_10 {background-position: 0 -423px;}
  #placesList .item .marker_11 {background-position: 0 -470px;}
  #placesList .item .marker_12 {background-position: 0 -516px;}
  #placesList .item .marker_13 {background-position: 0 -562px;}
  #placesList .item .marker_14 {background-position: 0 -608px;}
  #placesList .item .marker_15 {background-position: 0 -654px;}
  #pagination {
    margin: 10px auto;
    text-align: center;
  }
  
  #pagination a {
    display: inline-block;
    margin: 20px; /* 여기서 값을 조정하여 간격을 조절하세요 */
  }
  
  #pagination .on {
    font-weight: bold;
    cursor: default;
    color: #777;
  }

  /* 다크모드에도 글씨 보기 */
  .light-mode {
    color: black; 
  }
  </style>