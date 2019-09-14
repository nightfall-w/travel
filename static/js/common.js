function loadGrade(){
    $('.star-rating-read-only').raty({
        readOnly: true,
        round: {down: .2, full: .6, up: .8},
        half: true,
        space: false,
        score: function () {
            return $(this).attr('data-rating-score');
        }
    });
}

function getHotScheme(){
    new Vue({
        el: '#scheme_app',
        data () {
            return {
            schemesInfo: null
            }
        },
        watch:{
            schemesInfo:function(){
                this.$nextTick(function(){
                    loadGrade()
                })
            }
        },
        mounted () {
            axios
            .get('/info/schemes')
            .then(response => (this.schemesInfo = response.data))
            .catch(function (error) { // 请求失败处理
                console.log(error);
            });
        }
    })
}

function loadGrid(){
    /**
     * responsivegrid - layout grid
     */
    $('.grid').responsivegrid({
        gutter: '0',
        itemSelector: '.grid-item',
        'breakpoints': {
            'desktop': {
                'range': '1200-',
                'options': {
                    'column': 20,
                }
            },
            'tablet-landscape': {
                'range': '1000-1200',
                'options': {
                    'column': 20,
                }
            },
            'tablet-portrate': {
                'range': '767-1000',
                'options': {
                    'column': 20,
                }
            },
            'mobile-landscape': {
                'range': '-767',
                'options': {
                    'column': 10,
                }
            },
            'mobile-portrate': {
                'range': '-479',
                'options': {
                    'column': 10,
                }
            },
        }
    });
}
function getRecommendedSchemes(){
    new Vue({
        el: '#recommended_schemes',
        data () {
            return {
                schemesInfo: null,
            }
        },
        watch:{
            schemesInfo:function(){
                this.$nextTick(function(){
                    loadGrid()
                })
            }
        },
        mounted () {
            axios
            .get('/info/ScenicSpot')
            .then(response => (this.schemesInfo = response.data))
            .catch(function (error) { // 请求失败处理
                console.log(error);
            });
        }
    })
}