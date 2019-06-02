import React from 'react';
import styles from './index.css';
import { Menu, Icon, Layout, Row, Col } from 'antd';
import AnyImageForm from '@/components/AnyImageForm';
const { Header, Content, Footer, Sider } = Layout;
const { SubMenu } = Menu;

export default class App extends React.Component<any, any> {
  state = {
    current: 'file-image',
    previewImageUrl: undefined
  };

  handleClick = (e: { key: any }) => {
    this.setState({
      current: e.key,
    });
  };
  preview = (imageUrl:string)=>{
    this.setState({
      previewImageUrl: imageUrl
    })
  }
  render() {
    const HelpItem = (
      <span className="submenu-title-wrapper">
        <Icon type="question-circle" />
        帮助
      </span>
    );
    return (
      <Layout>
        <Header className={styles.header}>
          <Menu
            onClick={this.handleClick}
            selectedKeys={[this.state.current]}
            mode="horizontal"
            className={styles.headerMenu}
          >
            <Menu.Item key="file-image">
              <Icon type="file-image" />
              生成任意测试图像
            </Menu.Item>
            <Menu.Item key="file-video">
              <Icon type="video-camera" />
              生成任意测试视频
            </Menu.Item>
            <Menu.Item key="edit-image">
              <Icon type="edit" />
              图片格式转换
            </Menu.Item>
            <Menu.Item key="edit-video">
              <Icon type="scissor" />
              视频转换
            </Menu.Item>
            <SubMenu title={HelpItem}>
              <Menu.ItemGroup title="使用说明">
                <Menu.Item key="setting:1">生成任意测试图像</Menu.Item>
                <Menu.Item key="setting:2">生成任意测试视频</Menu.Item>
              </Menu.ItemGroup>
              <Menu.ItemGroup title="常见问题">
                <Menu.Item key="setting:3">图片格式转换</Menu.Item>
                <Menu.Item key="setting:4">视频转换</Menu.Item>
              </Menu.ItemGroup>
            </SubMenu>
            <Menu.Item key="mailto">
              <a href="mailto:woaiso@woaiso.com" rel="noopener noreferrer">
                <Icon type="mail" />
                联系我们
              </a>
            </Menu.Item>
          </Menu>
        </Header>
        <Layout>
          <Content className={styles.content}>
            <Row>
              <Col span={6}>
                <AnyImageForm preview={this.preview}/>
              </Col>
              <Col span={18}>
                <div style={{textAlign:'center'}}>预览</div>
                <div>
                  <div className={styles['preview-box']}>
                    <div className={styles['preview-inner']}>
                      {
                        this.state.previewImageUrl ? <img src={this.state.previewImageUrl} /> : <div className={styles['preview-tips-text']}>请在左侧调整您的配置，并点击预览</div>}

                    </div>
                  </div>
                </div>
              </Col>
            </Row>
          </Content>
        </Layout>
        <Footer className={styles.footer}>
          <div className={styles['footer-solgen']}>
            我们很乐意帮助到您, 关注并分享给更多需要的人!
          </div>
          <div className={styles['footer-wrap']}>
            <Row>
              <Col span={4}>
                <Icon type="global" /> 中文（简体）
              </Col>
              <Col span={6}>
                <div className={styles['footer-item']}>
                  <h2>关于我们</h2>
                  <div>
                    <a href="javascript:;">功能与优势</a>
                  </div>
                  <div>
                    <a href="javascript:;">我们的故事</a>
                  </div>
                  <div>
                    <a href="javascript:;">隐私政策</a>
                  </div>
                  <div>
                    <a href="javascript:;">联络我们</a>
                  </div>
                </div>
              </Col>
              <Col span={6}>
                <div className={styles['footer-item']}>
                  <h2>相关资源</h2>
                  <div>
                    <a target="_blank" href="https://dribbble.woaiso.com?utm_source=anyimage.xyz">Butterfly自动化工具平台</a>
                  </div>
                  <div>
                    <a target="_blank" href="https://lemon.woaiso.com?utm_source=anyimage.xyz">lemon爬虫与数据分析平台</a>
                  </div>
                  <div>
                    <a target="_blank" href="https://www.woaiso.com?utm_source=anyimage.xyz">我爱搜聚合搜索</a>
                  </div>
                  <div>
                    <a target="_blank" href="javascript:;">数据统计</a>
                  </div>
                </div>
              </Col>
              <Col span={8}>© AnyImage.xyz 2019 - 您的图片专家</Col>
            </Row>
          </div>
        </Footer>
      </Layout>
    );
  }
}
