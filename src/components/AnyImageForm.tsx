import React from 'react';
import { Form, Row, Col, Input, Select, InputNumber, Button, Icon, Popover } from 'antd';
import { SketchPicker } from 'react-color';
import qs from 'qs';

import styles from './form.less';

const { Option } = Select;
class AnyImageForm extends React.Component<any, any> {
  state = {
    bgColor: '#1890FF',
    displayBgColorPicker: false,
    textColor: '#FFFFFF',
    displayTextColorPicker: false,
  };
  preview = (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    this.props.form.validateFieldsAndScroll((err: any, values: any) => {
      if (!err) {
        this.action('preview', values);
      }
    });
  };
  download = (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    this.props.form.validateFieldsAndScroll((err: any, values: any) => {
      if (!err) {
        this.action('download', values);
      }
    });
  };
  action = (type:'download'|'preview', values:any) => {
    let download = 0;
    if(type === 'download'){
      download = 1;
    }
    values.download = download;
    const params = qs.stringify(values);
    const imageUrl = `https://anyimage.xyz/x?${params}`;
  }
  normFile = (e: { fileList: any }) => {
    if (Array.isArray(e)) {
      return e;
    }
    return e && e.fileList;
  };
  handleColorChange = (color: any) => {
    this.setState({
      bgColor: color.hex.toUpperCase(),
    });
    return false;
  };
  handleOpenColorPicker = () => {
    this.setState({
      displayBgColorPicker: true,
    });
    return false;
  };
  handleClose = () => {
    this.setState({
      displayBgColorPicker: false,
    });
  };
  handleTextColorChange = (color: any) => {
    this.setState({
      textColor: color.hex.toUpperCase(),
    });
    return false;
  };
  handleOpenTextColorPicker = () => {
    this.setState({
      displayTextColorPicker: true,
    });
    return false;
  };
  handleTextColorPickerClose = () => {
    this.setState({
      displayTextColorPicker: false,
    });
  };
  render() {
    const { getFieldDecorator } = this.props.form;
    const formItemLayout = {
      labelCol: { span: 8 },
      wrapperCol: { span: 16 },
    };
    return (
      <div className={styles['image-form']}>
        <Form {...formItemLayout}>
          <div>
            <h1 className={styles['form-title']}>请填写以下配置</h1>
          </div>
          <Form.Item label="宽度" help="支持范围：10 ~ 2048">
            {getFieldDecorator('width', {
              initialValue: 1080,
              rules: [{ required: true, message: '请输入正确的图片宽度!' }],
            })(<InputNumber min={10} max={2048} style={{ width: '100%' }} />)}
          </Form.Item>
          <Form.Item label="高度" help="支持范围：10 ~ 2048">
            {getFieldDecorator('height', {
              initialValue: 480,
              rules: [{ required: true, message: '请输入正确的图片高度!' }],
            })(<InputNumber min={10} max={2048} style={{ width: '100%' }} />)}
          </Form.Item>

          <Form.Item label="圆角" help="支持范围：0 ~ 100">
            {getFieldDecorator('radius', {
              initialValue: 0,
              rules: [{ required: false, message: '请输入正确的圆角大小!' }],
            })(<InputNumber min={0} max={100} style={{ width: '100%' }} />)}
          </Form.Item>

          <Form.Item label="内边距" help="参考格式：10 20 10 20">
            {getFieldDecorator('padding', {
              initialValue: 0,
              rules: [{ required: false, message: '请输入正确的圆角大小!' }],
            })(<Input style={{ width: '100%' }} />)}
          </Form.Item>

          <Form.Item label="背景颜色">
            {getFieldDecorator('bg_color', {
              initialValue: this.state.bgColor,
              rules: [],
            })(
              <Input
                addonAfter={<div className={styles['color-picker-button']} onClick={this.handleOpenColorPicker} style={{ background: this.state.bgColor }} />}
              />,
            )}
            <div className={styles['color-picker']}>
              {this.state.displayBgColorPicker ? (
                <div className={styles['color-picker']}>
                  <div className={styles.cover} onClick={this.handleClose} />
                  <SketchPicker color={this.state.bgColor} onChange={this.handleColorChange} />
                </div>
              ) : null}
            </div>
          </Form.Item>

          <Form.Item label="文本颜色">
          {getFieldDecorator('color', {
              initialValue: this.state.textColor,
              rules: [],
            })(
              <Input
                addonAfter={<div className={styles['color-picker-button']} onClick={this.handleOpenTextColorPicker} style={{ background: this.state.textColor }} />}
              />,
            )}
            <div className={styles['color-picker']}>
              {this.state.displayTextColorPicker ? (
                <div className={styles['color-picker']}>
                  <div className={styles.cover} onClick={this.handleTextColorPickerClose} />
                  <SketchPicker color={this.state.textColor} onChange={this.handleTextColorChange} />
                </div>
              ) : null}
            </div>
          </Form.Item>
          <Form.Item label="图片格式" hasFeedback={true}>
            {getFieldDecorator('format', {
              initialValue: 'png',
              rules: [{ required: false, message: '请选择一个导出的图片格式' }],
            })(
              <Select placeholder="请选择一个图片格式">
                <Option value="png">png</Option>
                <Option value="gif">gif</Option>
                <Option value="jpg">jpg</Option>
                <Option value="jpeg">jpeg</Option>
              </Select>,
            )}
          </Form.Item>

          <Form.Item label="文件大小(KB)" help="默认使用自动生成的文件大小">
            {getFieldDecorator('volume', {
              initialValue: 0,
              rules: [{ required: false, message: '请输入正确的文件大小!' }],
            })(<InputNumber min={0} max={2048} style={{ width: '100%' }} />)}
          </Form.Item>

          <Form.Item label="文本">
            {getFieldDecorator('text', {
              initialValue: 'anyimage.xyz',
              rules: [],
            })(<Input />)}
          </Form.Item>
          <Row gutter={8}>
            <Col span={12}>
              <div className={styles['gutter-box']}>
                <Button type="default" icon="eye" size="large" style={{ width: '100%' }} onClick={this.preview}>
                  预览
                </Button>
              </div>
            </Col>
            <Col span={12}>
              <div className={styles['gutter-box']}>
                <Button type="primary" icon="download" size="large" style={{ width: '100%' }} onClick={this.download}>
                  下载
                </Button>
              </div>
            </Col>
          </Row>
        </Form>
      </div>
    );
  }
}

export default Form.create({ name: 'any_image_form' })(AnyImageForm);
